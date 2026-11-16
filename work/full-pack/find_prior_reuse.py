from pathlib import Path
import json,importlib.util,collections
w=Path(r'E:\minecratf\minecratf_repo_git\Tensura_Neo_Otherworld_Thai\work\full-pack');spec=importlib.util.spec_from_file_location('mtt',Path(r'E:\minecratf\minecratf_repo_git\modpack-thai-translator\scripts\mtt.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);src=json.loads((w/'source.json').read_text(encoding='utf-8'))['items'];tr=m.all_translations(str(w));reuse={};origins={}
for old in [Path(r'E:\minecratf\projects\BeyondTheSkybox-Thai\work'),Path(r'E:\minecratf\projects\ThisIsUnreal-Thai-Context\mtt-review')]:
 if not (old/'source.json').exists():continue
 osrc=json.loads((old/'source.json').read_text(encoding='utf-8'))['items'];otrans=m.all_translations(str(old))
 for k,v in otrans.items():
  if k in src and k not in tr and src[k]['en']==osrc.get(k,{}).get('en') and not m.check_item(k,src[k]['en'],v,{})[0]:reuse[k]=v;origins[k]=str(old)
print('Exact source+key reusable candidates from prior local projects:',len(reuse),dict(collections.Counter(k.split('|')[1] for k in reuse)))
(w/'prior-project-reuse-candidates.json').write_text(json.dumps({'items':reuse,'origins':origins},ensure_ascii=False,indent=2),encoding='utf-8')
