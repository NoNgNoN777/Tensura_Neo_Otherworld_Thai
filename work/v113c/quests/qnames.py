"""qnames.py N : write qtNN.json = English copy for every key, then overlay ovNN.json (Thai overrides)."""
import json,sys,subprocess
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
W=Path(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\v113c\quests')
N=int(sys.argv[1])
out=subprocess.run([sys.executable,'-I',str(W/'q.py'),'dump',str(N)],capture_output=True,text=True,encoding='utf-8').stdout
keys=[l.split(' = ',1)[0] for l in out.splitlines() if not l.startswith('   ') and ' = ' in l]
S=json.load(open(W/'source.json',encoding='utf-8'))['items']
ov=json.load(open(W/f'ov{N:02d}.json',encoding='utf-8'))
d={k:S[k] for k in keys};d.update(ov)
json.dump(d,open(W/f'qt{N:02d}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('keys',len(keys),'overrides',len(ov))
