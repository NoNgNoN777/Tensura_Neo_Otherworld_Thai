import json,glob,re,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
thai=re.compile(r'[\u0e00-\u0e7f]');cjk=re.compile(r'[\u4e00-\u9fff]')
R=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\translation-src\lang'
src=json.load(open(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\source.json',encoding='utf-8'))['items']
tot=0;nothai=[];cj=[];dup=[];odd=[]
for f in glob.glob(R+'/*/lang/th_th.json'):
    ns=f.replace('\\','/').split('/')[-3]
    d=json.load(open(f,encoding='utf-8'))
    for k,v in d.items():
        tot+=1
        if not isinstance(v,str): continue
        if cjk.search(v) and not thai.search(v): cj.append((ns,k,v[:60]))
        if not thai.search(v) and len(re.sub(r'%[0-9$]*[sd]|§.|\$\([^)]*\)','',v))>45 and ' ' in v: nothai.append((ns,k,v[:70]))
        if re.search(r'([\u0e00-\u0e7f]{3,})\1',v): dup.append((ns,k,v[:80]))
        if re.search(r'เชื่อง|\bของของ|ที่ที่|แล้วแล้ว|ได้ได้|เป็นเป็น',v): odd.append((ns,k,v[:80]))
print('total',tot,'noThaiLong',len(nothai),'cjkOnly',len(cj),'dupThai',len(dup))
for n,l in (('nothai',nothai),('cjk',cj),('dup',dup)):
    print('==',n)
    for x in l[:25]: print(x)
c=collections.Counter(a[0] for a in nothai);print(c.most_common(15))
