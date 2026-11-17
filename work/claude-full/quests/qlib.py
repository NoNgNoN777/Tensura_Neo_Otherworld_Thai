import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
R=r'D:\minecraft\Tensura_Neo_Otherworld_Thai'
W=R+r'\work\claude-full\quests'
S=json.load(open(R+r'\translation-src\quests\source.json',encoding='utf-8'))['items']
def T(): return json.load(open(W+r'\translations.json',encoding='utf-8'))
def size(v): return sum(len(x) for x in v)+len(v)*4 if isinstance(v,list) else len(v)
def pending():
    t=T()['items']; return [k for k in S if k not in t]
def batches(limit=9000):
    out=[];cur=[];n=0
    for k in [k for k in S if k not in json.load(open(R+r'\translation-src\quests\translations.json',encoding='utf-8'))['items']]:
        sz=size(S[k])+len(k)
        if cur and n+sz>limit: out.append(cur);cur=[];n=0
        cur.append(k);n+=sz
    if cur: out.append(cur)
    return out
def special(text):
    lines=text if isinstance(text,list) else [text];out=[]
    for line in lines:
        out.extend(re.findall(r'\{(?:image|translate):[^}]+\}',line))
        try: obj=json.loads(line)
        except (ValueError,TypeError): continue
        def walk(x):
            if isinstance(x,dict):
                for k,v in x.items():
                    if k in ('clickEvent','hoverEvent'): out.append(json.dumps({k:v},sort_keys=True,ensure_ascii=False))
                    else: walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(obj)
    return sorted(out)
