import json,sys
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
n=sys.argv[1]
out={}
for l in open(W+rf'\tmp\d{n}.txt',encoding='utf-8'):
    if ' = ' in l:
        k,v=l.rstrip('\n').split(' = ',1); out[k]=json.loads(v)
json.dump(out,open(W+rf'\tmp\t{n}.json','w',encoding='utf-8'),ensure_ascii=False); print(len(out))
