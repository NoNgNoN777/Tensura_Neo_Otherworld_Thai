import sys,json
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\patch')
from plib import *
n=int(sys.argv[1]);bs=batches();keys=bs[n-1];S=collect()
# input file keyed by short id (after patchouli_books/, '/en_us/' -> '|')
short={k.split('patchouli_books/')[1].replace('/en_us/','|'):k for k in keys}
d=json.load(open(BASE+rf'\pt{n:02d}.json',encoding='utf-8'))
miss=[s for s in short if s not in d];extra=[s for s in d if s not in short]
print('keys',len(keys),'missing',miss,'extra',extra)
errs=[]
for s,v in d.items():
    if s not in short: continue
    en=S[short[s]]
    if MAC.findall(en)!=MAC.findall(v): errs.append((s,'macro',MAC.findall(en),MAC.findall(v)))
for e in errs: print('ERR',e)
if not errs and not miss and not extra:
    t=load_tr()
    for s,v in d.items(): t[short[s]]=v
    json.dump(t,open(BASE+r'\translations.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('merged',len(t))
