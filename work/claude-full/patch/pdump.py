import sys,json
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\patch')
from plib import *
bs=batches();n=int(sys.argv[1])
if n==0: print(len(bs),sum(len(b) for b in bs)); sys.exit()
S=collect()
for k in bs[n-1]:
    print(k.split('patchouli_books/')[1].replace('/en_us/','|'),'=',json.dumps(S[k],ensure_ascii=False))
