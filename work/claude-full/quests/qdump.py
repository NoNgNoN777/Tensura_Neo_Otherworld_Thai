import sys,json
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\quests')
from qlib import *
bs=batches()
n=int(sys.argv[1])
if n==0: print(len(bs)); sys.exit()
for k in bs[n-1]: print(k,'=',json.dumps(S[k],ensure_ascii=False))
