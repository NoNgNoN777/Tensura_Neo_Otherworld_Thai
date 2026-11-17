"""Apply the selected TNO built-in compatibility pack after mtt scan/extract.

The generic scanner does not read mod/<id>:resourcepacks/<name> entries.
Do not run this for a different instance or blindly apply every built-in pack.
"""
from pathlib import Path
import json,zipfile
w=Path(__file__).resolve().parent
p=json.loads((w/'project.json').read_text(encoding='utf-8'))
inst=Path(p['instance'])
opt=inst/'options.txt'
assert (not opt.exists()) or 'mod/tensura_tno:resourcepacks/greatsage_patches' in opt.read_text(encoding='utf-8')
jar=next((inst/'mods').glob('tensura_tno-*.jar'))
cache=json.loads((w/'cache/lang_sources.json').read_text(encoding='utf-8'))
source=json.loads((w/'source.json').read_text(encoding='utf-8'))
resolved=json.loads((w/'resolved.json').read_text(encoding='utf-8'))
changed=[]
with zipfile.ZipFile(jar) as z:
 for name in z.namelist():
  prefix='resourcepacks/greatsage_patches/assets/'
  if not name.startswith(prefix) or not name.endswith('/lang/en_us.json'):continue
  ns=name[len(prefix):].split('/')[0]
  for k,en in json.loads(z.read(name)).items():
   old=cache['en'].setdefault(ns,{}).get(k)
   owner=f'pack:{jar.name}!{name}'
   cache['en'][ns][k]=en;cache['origin'].setdefault(ns,{})[k]=owner
   ik=f'lang|{ns}|{k}'
   if ik in source['items']:
    if source['items'][ik]['en']!=en:
     changed.append({'key':ik,'previous':source['items'][ik]['en'],'en':en})
     resolved.pop(ik,None)
    source['items'][ik]['en']=en;source['items'][ik]['origin']=owner;source['items'][ik]['generic']=False
for path,data in [('cache/lang_sources.json',cache),('source.json',source),('resolved.json',resolved)]:
 (w/path).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
# Re-running is idempotent and must not erase the original source-difference audit.
if changed:(w/'builtin-source-changes.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf-8')
print('Changed selected source keys:',len(changed))
for r in changed:print(r['key'],r['en'])
