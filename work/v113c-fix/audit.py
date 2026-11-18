"""Audit every lang key added/changed versus git HEAD."""
import json, os, re, sys, subprocess, importlib.util, collections, glob
sys.stdout.reconfigure(encoding='utf-8')
W = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(W, '..', '..'))
sp = importlib.util.spec_from_file_location('mtt', os.path.join(R, '..', 'modpack-thai-translator', 'scripts', 'mtt.py'))
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
cache = json.load(open(os.path.join(R, 'work', 'v113c', 'cache', 'lang_sources.json'), encoding='utf-8'))['en']
prob = collections.defaultdict(list); total = 0; files = 0
for p in sorted(glob.glob(os.path.join(R, 'translation-src', 'lang', '*', 'lang', 'th_th.json'))):
    ns = p.split(os.sep)[-3]; rel = os.path.relpath(p, R).replace(os.sep, '/')
    try:
        cur = json.load(open(p, encoding='utf-8-sig'))
    except Exception as e:
        prob['invalid json'].append(rel); continue
    old = subprocess.run(['git', '-C', R, 'show', 'HEAD:' + rel], capture_output=True).stdout
    old = json.loads(old.decode('utf-8-sig')) if old else {}
    lost = [k for k in old if k not in cur]
    if lost: prob['keys removed'].append((rel, lost[:3]))
    en = cache.get(ns, {})
    ch = [k for k in cur if old.get(k) != cur[k]]
    if ch: files += 1
    for k in ch:
        total += 1; th = cur[k]; e = en.get(k)
        if not isinstance(th, str) or not th.strip(): prob['empty'].append((ns, k)); continue
        if e is None: prob['key not in English source'].append((ns, k)); continue
        errs, _ = m.check_item('lang|%s|%s' % (ns, k), e, th, {})
        if errs: prob['mtt error'].append((ns, k, errs, th))
        if e.count('\n') != th.count('\n'): prob['newline count'].append((ns, k))
        if '\\n' in th and '\\n' not in e: prob['literal \\n'].append((ns, k))
        if (e[:1].isspace(), e[-1:].isspace()) != (th[:1].isspace(), th[-1:].isspace()): prob['edge space'].append((ns, k, repr(e[:12]), repr(th[:12])))
        if re.search(r'[§&][lo]', th): prob['bold/italic code'].append((ns, k))
        if re.search(r'([ก-๛]{2,})\1', th): prob['repeated word?'].append((ns, k, th[:80]))
        if re.search(r'[一-鿿]', th) and not re.search(r'[一-鿿]', e): prob['CJK added'].append((ns, k))
print('changed/added keys checked', total, 'in', files, 'files')
for t, v in prob.items():
    print('==', t, len(v))
    for x in v[:8]: print('   ', x)
