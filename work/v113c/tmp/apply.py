import json,sys,subprocess,os
sys.stdout.reconfigure(encoding='utf-8')
W='D:/minecraft/Tensura_Neo_Otherworld_Thai/work/v113c'
MTT=r'D:\minecraft\modpack-thai-translator\scripts\mtt.py'
n=sys.argv[1]
if len(sys.argv)>2 and sys.argv[2]=='dump':
    d=json.load(open(f'{W}/batches/todo_{n}.json',encoding='utf-8'))
    prev=d.get('previous_translation',{})
    for k,v in d['items'].items():
        t=k.split('|',2)[2]
        print(t,'=',json.dumps(v,ensure_ascii=False))
        if k in prev: print('   PREV =',json.dumps(prev[k],ensure_ascii=False))
    sys.exit()
d=json.load(open(f'{W}/batches/todo_{n}.json',encoding='utf-8'))['items']
T=json.load(open(f'{W}/tmp/t{n}.json',encoding='utf-8'))
out={};miss=[];extra=set(T)
for k in d:
    t=k.split('|',2)[2]
    if t in T:out[k]=T[t];extra.discard(t)
    else:miss.append(t)
print('items',len(d),'missing',len(miss),'extra',len(extra))
for m in miss[:20]:print(' MISSING',m)
for m in list(extra)[:10]:print(' EXTRA',m)
if miss:sys.exit(1)
json.dump({'items':out},open(f'{W}/batches/done_{n}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
env=dict(os.environ,PYTHONIOENCODING='utf-8')
r=subprocess.run([sys.executable,MTT,'validate','--work',W,'--batch',n],capture_output=True,text=True,encoding='utf-8',env=env)
print(r.stdout.strip())
txt=open(f'{W}/validate.md',encoding='utf-8').read()
print('\n'.join(l for l in txt.splitlines() if 'error' in l.lower())[:3000])
