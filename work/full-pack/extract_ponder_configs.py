from pathlib import Path
import json,collections
w=Path(r'E:\minecratf\minecratf_repo_git\Tensura_Neo_Otherworld_Thai\work\full-pack');inst=Path(r'D:\minecraft\Instances\Tensura Neo Otherworld');rows=[];files={}
def walk(x,path,p):
 if isinstance(x,dict):
  if isinstance(x.get('en_us'),str):rows.append({'file':str(p.relative_to(inst)),'path':path+['en_us'],'english':x['en_us']})
  for k,v in x.items():walk(v,path+[k],p)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,path+[i],p)
for p in (inst/'config/ponderer/scripts').rglob('*.json'):
 d=json.loads(p.read_text(encoding='utf-8-sig'));files[str(p.relative_to(inst))]=d;walk(d,[],p)
(w/'ponder-config-source.json').write_text(json.dumps({'items':rows,'files':files},ensure_ascii=False,indent=2),encoding='utf-8');print('Ponder config:',len(files),'files',len(rows),'strings',sum(len(r['english']) for r in rows),'characters')
for i,r in enumerate(rows[:35]):print(i,repr(r['english']))
