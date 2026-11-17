"""Build tNNN.json from previous translations with line/substring removals.
usage: fromprev.py NNN  (reads tmp/rNNN.json: {tailkey: [[old,new],...]} replacements applied to PREV;
       plus optional tmp/xNNN.json with direct translations merged on top)"""
import json,sys,os
sys.stdout.reconfigure(encoding='utf-8')
W='D:/minecraft/Tensura_Neo_Otherworld_Thai/work/v113c'
n=sys.argv[1]
d=json.load(open(f'{W}/batches/todo_{n}.json',encoding='utf-8'))
prev={k.split('|',2)[2]:v for k,v in d.get('previous_translation',{}).items()}
r=json.load(open(f'{W}/tmp/r{n}.json',encoding='utf-8')) if os.path.exists(f'{W}/tmp/r{n}.json') else {}
x=json.load(open(f'{W}/tmp/x{n}.json',encoding='utf-8')) if os.path.exists(f'{W}/tmp/x{n}.json') else {}
out={}
for k,reps in r.items():
    s=prev[k]
    for a,b in reps:
        assert a in s,(k,a)
        s=s.replace(a,b,1)
    NL3=chr(10)*3;NL2=chr(10)*2
    while NL3 in s: s=s.replace(NL3,NL2)
    out[k]=s
out.update(x)
json.dump(out,open(f'{W}/tmp/t{n}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('wrote',len(out))
