"""q.py dump N | apply N | count
Batches over todo.json (~7000 chars of English each).
In qtNN.json a value is either the full Thai (str/list) or {"old": [[a,b],...]} = apply replacements to the old Thai
(for lists, each replacement is applied to the joined text with \n and split back)."""
import json,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
R=Path(r'D:\minecraft\Tensura_Neo_Otherworld_Thai');W=R/'work/v113c/quests'
sys.path.insert(0,str(R/'tools'));import build_pack as bp
S=json.load(open(W/'source.json',encoding='utf-8'))['items']
OS=json.load(open(R/'translation-src/quests/source.json',encoding='utf-8'))['items']
OT=json.load(open(R/'translation-src/quests/translations.json',encoding='utf-8'))['items']
todo=json.load(open(W/'todo.json'))
bs=[];cur=[];n=0
for k in todo:
    l=len(json.dumps(S[k]))+(len(json.dumps(OS[k])) if k in OS else 0)
    if n+l>7000 and cur: bs.append(cur);cur=[];n=0
    cur.append(k);n+=l
if cur: bs.append(cur)
cmd=sys.argv[1]
if cmd=='count': print(len(bs));sys.exit()
N=int(sys.argv[2]);keys=bs[N-1]
J=lambda x:json.dumps(x,ensure_ascii=False)
if cmd=='dump':
    for k in keys:
        print(k,'=',J(S[k]))
        if k in OS:
            print('   OLD_EN =',J(OS[k]));print('   OLD_TH =',J(OT[k]))
    sys.exit()
d=json.load(open(W/f'qt{N:02d}.json',encoding='utf-8'))
miss=[k for k in keys if k not in d];extra=[k for k in d if k not in keys]
print('keys',len(keys),'missing',miss,'extra',extra)
errs=[];out={}
for k,v in d.items():
    if k not in S: continue
    if isinstance(v,dict):
        old=OT[k];s='\n'.join(old) if isinstance(old,list) else old
        for a,b in v['old']:
            if a not in s: errs.append((k,'old text not found',a));break
            s=s.replace(a,b,1)
        v=s.split('\n') if isinstance(S[k],list) else s
    en=S[k];out[k]=v
    if type(en)!=type(v): errs.append((k,'type'));continue
    if isinstance(en,list) and len(en)!=len(v): errs.append((k,'len %d vs %d'%(len(en),len(v))));continue
    if bp.special(en)!=bp.special(v): errs.append((k,'directive'))
    if isinstance(en,list):
        for a,b in zip(en,v):
            if (a=='')!=(b==''): errs.append((k,'blank-line mismatch'));break
for e in errs: print('ERR',e)
if not errs and not miss:
    t=json.load(open(W/'translations.json',encoding='utf-8'));t['items'].update(out)
    json.dump(t,open(W/'translations.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('merged; total',len(t['items']),'/',len(S))
