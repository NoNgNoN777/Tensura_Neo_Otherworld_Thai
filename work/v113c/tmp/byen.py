"""Write tmp/xNNN.json from an English->Thai dict tmp/eNNN.json (many keys share one English text)."""
import json,sys
sys.stdout.reconfigure(encoding='utf-8')
W='D:/minecraft/Tensura_Neo_Otherworld_Thai/work/v113c'
n=sys.argv[1]
d=json.load(open(f'{W}/batches/todo_{n}.json',encoding='utf-8'))['items']
e=json.load(open(f'{W}/tmp/e{n}.json',encoding='utf-8'))
out={};miss=[]
for k,v in d.items():
    t=k.split('|',2)[2]
    if v in e: out[t]=e[v]
    else: miss.append(t)
json.dump(out,open(f'{W}/tmp/x{n}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('mapped',len(out),'missing',miss)
