import json,sys
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
PFX='foxablazeaqzl_wiki.wiki.'
def run(N,D,fb=None):
    n=f'{N:03d}'
    keys=[];out={}
    for l in open(W+rf'\tmp\d{n}.txt',encoding='utf-8'):
        if ' = ' not in l: continue
        k,v=l.rstrip('\n').split(' = ',1)
        keys.append(k)
        a=k[len(PFX):] if k.startswith(PFX) else k
        if a in D: out[k]=D[a]
        elif fb:
            r=fb(a,json.loads(v))
            if r is not None: out[k]=r
    print('keys',len(keys),'out',len(out),[k.split('wiki.')[-1] for k in keys if k not in out])
    json.dump(out,open(W+rf'\tmp\t{n}.json','w',encoding='utf-8'),ensure_ascii=False)
