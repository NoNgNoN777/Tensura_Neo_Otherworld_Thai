import sys,json
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\quests')
from qlib import *
n=int(sys.argv[1]); bs=batches(); keys=bs[n-1]
d=json.load(open(W+rf'\qt{n:02d}.json',encoding='utf-8'))
miss=[k for k in keys if k not in d]; extra=[k for k in d if k not in keys]
print('keys',len(keys),'missing',miss,'extra',extra)
errs=[]
for k,v in d.items():
    if k not in S: continue
    en=S[k]
    if type(en)!=type(v): errs.append((k,'type')); continue
    if isinstance(en,list) and len(en)!=len(v): errs.append((k,'len %d vs %d'%(len(en),len(v)))); continue
    if special(en)!=special(v): errs.append((k,'directive'))
    if isinstance(en,list):
        for a,b in zip(en,v):
            if (a=='')!=(b==''): errs.append((k,'blank-line mismatch'));break
for e in errs: print('ERR',e)
if not errs and not miss:
    t=T(); t['items'].update(d)
    json.dump(t,open(W+r'\translations.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('merged; total',len(t['items']))
