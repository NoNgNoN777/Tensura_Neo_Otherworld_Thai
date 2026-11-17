import json,glob,os,re,sys
sys.stdout.reconfigure(encoding='utf-8')
BASE='D:/minecraft/Tensura_Neo_Otherworld_Thai/work/v113c/patch'
SRC=BASE+r'\src'
TK={'name','title','text','description','time'}
MAC=re.compile(r'\$\([^)]*\)')
def files():
    return sorted(p.replace(os.sep,'/') for p in glob.glob(SRC+'/**/*.json',recursive=True))
def rel(f): return f[len(SRC.replace(os.sep,'/'))+1:]
def collect():
    out={}
    for f in files():
        d=json.load(open(f,encoding='utf-8'))
        def walk(x,path):
            if isinstance(x,dict):
                for a,b in x.items():
                    if a in TK and isinstance(b,str): out[rel(f)+'::'+'/'.join(map(str,path+[a]))]=b
                    else: walk(b,path+[a])
            elif isinstance(x,list):
                for i,b in enumerate(x): walk(b,path+[i])
        walk(d,[])
    return out
def batches(limit=9000):
    S=collect();bs=[];cur=[];n=0
    for k,v in S.items():
        if n+len(v)>limit and cur: bs.append(cur);cur=[];n=0
        cur.append(k);n+=len(v)+len(k)
    if cur: bs.append(cur)
    return bs
def load_tr():
    p=BASE+r'\translations.json'
    return json.load(open(p,encoding='utf-8')) if os.path.exists(p) else {}
