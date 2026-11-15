"""Read-only checks of the current translation work; reports go to work/audit/."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'


def read(path):
    def unique(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise ValueError(f'Duplicate JSON key: {path}: {key}')
            obj[key] = value
        return obj
    raw = path.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        raise ValueError(f'Unexpected BOM: {path}')
    return json.loads(raw.decode('utf-8'), object_pairs_hook=unique)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tool', type=Path, required=True)
    parser.add_argument('--label', choices=['baseline', 'final'], required=True)
    args = parser.parse_args()
    source = read(WORK / 'source.json')['items']
    project = read(WORK / 'project.json')
    resolved = read(WORK / 'resolved.json')
    merged = {key: value['th'] for key, value in resolved.items()}
    batches = []
    for path in sorted((WORK / 'batches').glob('done_*.json')):
        todo = read(path.with_name(path.name.replace('done_', 'todo_')))['items']
        done = read(path)['items']
        batches.append((path.name, todo, done))
        merged.update(done)
    results = []

    def check(number, title, errors, details):
        results.append(dict(round=number, check=title, passed=not errors,
                            errors=errors, details=details))

    errors = []
    for name, todo, done in batches:
        if todo.keys() != done.keys():
            errors.append(name + ': key sets differ')
        for key, value in done.items():
            if key not in source or todo.get(key) != source[key]['en']:
                errors.append(name + ': stale source: ' + key)
            if not isinstance(value, str) or not value.strip():
                errors.append(name + ': empty/non-string: ' + key)
    check(1, 'JSON, batch coverage and saved source', errors,
          dict(batches=len(batches), translated=len(merged), selected=len(source)))

    errors, jars = [], {}
    for key, entry in source.items():
        origin = entry['origin']
        if origin not in jars:
            with zipfile.ZipFile(Path(project['instance']) / 'mods' / origin) as jar:
                jars[origin] = json.loads(jar.read('assets/tensura/lang/en_us.json'))
        if jars[origin].get(entry['key']) != entry['en']:
            errors.append(key)
    check(2, 'Saved English against installed JAR', errors, dict(entries=len(source), jars=len(jars)))

    errors = []
    pattern = r'%(?:\d+\$)?[A-Za-z%]|\{[^{}]+\}'
    for key, value in merged.items():
        if Counter(re.findall(pattern, source[key]['en'])) != Counter(re.findall(pattern, value)):
            errors.append(key)
    check(3, 'Placeholders and brace tokens', errors, dict(entries=len(merged)))

    errors = []
    for key, value in merged.items():
        if Counter(re.findall(r'\d+', source[key]['en'])) != Counter(re.findall(r'\d+', value)):
            errors.append(key)
    check(4, 'Numeric tokens and multiplicity', errors, dict(entries=len(merged)))

    errors = []
    for key, value in merged.items():
        original = source[key]['en']
        if '\ufffd' in value or any(ord(c) < 32 and c not in '\n\r\t' for c in value):
            errors.append(key + ': invalid character')
        if Counter(re.findall(r'[§&][0-9a-fk-or]', original)) != Counter(re.findall(r'[§&][0-9a-fk-or]', value)):
            errors.append(key + ': formatting codes')
        if value.count('\n') != original.count('\n'):
            errors.append(key + ': newline count')
    check(5, 'Encoding, controls, formatting and line breaks', errors, dict(entries=len(merged)))

    names = ['Dwargon', 'Stellar Gold coin', 'Gold coin', 'Unique Skill', 'Harvest Festival',
             'Demon Lord Seed', 'True Demon Lord', 'EP', 'XP', 'Magic Ore', 'Labyrinth']
    errors, unchanged = [], []
    for key, value in merged.items():
        original = source[key]['en']
        if original == value:
            unchanged.append(key)
        for name in names:
            if name in original and name not in value:
                errors.append(key + ': missing ' + name)
    check(6, 'Selected glossary names and untranslated text', errors,
          dict(names=names, unchanged=unchanged, note='Targeted glossary check; not a complete semantic proof'))

    inert = 'lang|tensura|tooltip.tensura.charybdis_core.inert'
    inactive = 'lang|tensura|tooltip.tensura.charybdis_core.inactive'
    dead = 'lang|tensura|enchantment.tensura.dead_end_rainbow.desc'
    errors = []
    if merged[inert] == merged[inactive]:
        errors.append('Inert and Inactive use the same Thai despite distinct COOLDOWN/INACTIVE branches')
    if 'หากเป็นไปตามเงื่อนไข' in merged[dead]:
        errors.append('Dead End Rainbow introduces unspecified conditions beyond Ideally')
    check(7, 'Context review regressions', errors,
          dict(memory_entries=len(resolved), evidence='CharybdisCoreBlock javap: COOLDOWN -> inert; original Dead End Rainbow English'))

    run = subprocess.run(['python', str(args.tool), 'validate', '--work', str(WORK)],
                         capture_output=True, encoding='utf-8', errors='replace')
    report = (WORK / 'validate.md').read_text(encoding='utf-8')
    check(8, 'Toolkit full validation', [] if run.returncode == 0 else [run.stderr, run.stdout],
          dict(stdout=run.stdout.strip(), report=report))

    archive = WORK / 'build/resourcepack/ZZ_Tensura_Neo_Otherworld_Thai.zip'
    with zipfile.ZipFile(archive) as zip_file:
        entries = zip_file.namelist()
        errors = []
        if len(entries) != len(set(entries)) or zip_file.testzip() is not None:
            errors.append('Duplicate ZIP member or CRC failure')
        if any(Path(name).is_absolute() or '..' in Path(name).parts or name.endswith('.jar') for name in entries):
            errors.append('Unsafe path or bundled JAR')
        metadata = json.loads(zip_file.read('pack.mcmeta'))
        if metadata['pack']['pack_format'] != 34:
            errors.append('Unexpected resource pack format for Minecraft 1.21.1')
        if 'assets/tensura/lang/en_us.json' in entries:
            errors.append('Unexpected English override')
        output = json.loads(zip_file.read('assets/tensura/lang/th_th.json'))
    check(9, 'ZIP CRC, paths, metadata and delivery scope', errors, dict(members=entries))

    expected = {key.split('|', 2)[2]: value for key, value in merged.items()}
    folder = read(WORK / 'build/resourcepack/Tensura_Neo_Otherworld_Thai/assets/tensura/lang/th_th.json')
    check(10, 'ZIP/folder parity with all translations',
          [] if expected == output == folder else ['Build output does not match current translations'],
          dict(expected=len(expected), output=len(output), remaining=len(source)-len(merged),
               zip_sha256=hashlib.sha256(archive.read_bytes()).hexdigest()))

    destination = WORK / 'audit'
    destination.mkdir(exist_ok=True)
    (destination / f'{args.label}.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for result in results:
        print(f"{result['round']:02} {'PASS' if result['passed'] else 'FAIL'} {result['check']}")
        for error in result['errors']:
            print('  ' + error)
    raise SystemExit(0 if all(result['passed'] for result in results) else 1)


if __name__ == '__main__':
    main()
