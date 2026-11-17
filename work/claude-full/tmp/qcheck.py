import json,re,sys,random
sys.stdout.reconfigure(encoding='utf-8')
S=json.load(open(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\translation-src\quests\source.json',encoding='utf-8'))['items']
T=json.load(open(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\translation-src\quests\translations.json',encoding='utf-8'))['items']
col=re.compile(r'&#[0-9A-Fa-f]{6}|&[0-9a-fk-or]')
num=re.compile(r'\d[\d,\.]*')
bad=0
for k,en in S.items():
    a=en if isinstance(en,list) else [en]; b=T[k] if isinstance(T[k],list) else [T[k]]
    ca=[col.findall(x) for x in a]; cb=[col.findall(x) for x in b]
    if ca!=cb:
        bad+=1
        if bad<=12: print('COLOR',k,ca[:3],cb[:3])
print('color mismatches',bad)
nb=0
for k,en in S.items():
    a=' '.join(en) if isinstance(en,list) else en; b=' '.join(T[k]) if isinstance(T[k],list) else T[k]
    na=sorted(x.rstrip('.,') for x in num.findall(re.sub(r'\{[^}]*\}|"value": "[^"]*"|&#[0-9A-Fa-f]{6}','',a)))
    nb_=sorted(x.rstrip('.,') for x in num.findall(re.sub(r'\{[^}]*\}|"value": "[^"]*"|&#[0-9A-Fa-f]{6}','',b)))
    if na!=nb_ and len(na)<12:
        nb+=1
        if nb<=15: print('NUM',k,na,nb_)
print('number mismatches',nb)
