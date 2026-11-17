"""Build quests/source.json (items + spans) from the 1.1.3c en_us.snbt, and a draft translation map.
Draft = old translation where the English is unchanged; todo list = new or changed keys."""
import json,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
R=Path(r'D:\minecraft\Tensura_Neo_Otherworld_Thai')
sys.path.insert(0,str(R/'tools'));import build_pack as bp
W=R/'work/v113c/quests';W.mkdir(exist_ok=True)
src=Path(r'D:\game2\Instances\Tensura Neo Otherworld\config\ftbquests\quests\lang\en_us.snbt').read_text(encoding='utf-8-sig')
dec=json.JSONDecoder();i=0;items={};spans={}
def ws():
    global i
    while i<len(src) and (src[i].isspace() or src[i]==','):i+=1
def val():
    global i
    ws()
    if src[i]=='[':
        i+=1;out=[];ws()
        while src[i]!=']':out.append(val());ws()
        i+=1;return out
    v,i2=dec.raw_decode(src,i);i=i2;return v
ws();assert src[i]=='{';i+=1;ws()
while src[i]!='}':
    m=re.match(r'([a-z_][a-z0-9_]*\.[^\s{}:]+)\s*:',src[i:]);k=m[1];i+=m.end();ws()
    s=i;items[k]=val();spans[k]={'start':s,'end':i};ws()
assert bp.parse_quest(src)==items
for k,sp in spans.items():
    t=src[sp['start']:sp['end']]
    assert bp.parse_quest('{'+k+':'+t+'}')[k]==items[k],k
(W/'original-en_us.snbt').write_text(src,encoding='utf-8',newline='')
json.dump({'items':items,'spans':spans},open(W/'source.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
old=json.load(open(R/'translation-src/quests/source.json',encoding='utf-8'))['items']
oldt=json.load(open(R/'translation-src/quests/translations.json',encoding='utf-8'))['items']
draft={k:oldt[k] for k in items if k in old and old[k]==items[k]}
todo=[k for k in items if k not in draft]
json.dump({'items':draft},open(W/'translations.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
json.dump(todo,open(W/'todo.json','w'),indent=0)
print('items',len(items),'reused',len(draft),'todo',len(todo))
