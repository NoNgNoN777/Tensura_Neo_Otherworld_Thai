import sys,json
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\quests')
from qlib import *
n=int(sys.argv[1]); keys=batches()[n-1]
ov=json.load(open(W+rf'\ov{n:02d}.json',encoding='utf-8'))
out={k:ov.get(k,S[k]) for k in keys}
json.dump(out,open(W+rf'\qt{n:02d}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'overrides',len(ov))
