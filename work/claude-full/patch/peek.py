import json,glob,re,sys,collections,os
sys.stdout.reconfigure(encoding='utf-8')
cjk=re.compile(r'[一-鿿]')
c=collections.Counter()
fs=[p.replace(os.sep,'/') for p in glob.glob('src/**/*.json',recursive=True)]
for f in fs:
    s=open(f,encoding='utf-8').read()
    book=f.split('patchouli_books/')[1].split('/')[0]
    c[(book,bool(cjk.search(s)))]+=1
print(c)
for key in ('alchemy_furnace.json','introduction.json'):
    f=[x for x in fs if x.endswith(key)][0];print(f);print(open(f,encoding='utf-8').read()[:1200])
