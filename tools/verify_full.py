"""Verify the full build. Compares CONTENT (not ZIP bytes) so it also works on Python 3.14 and with git autocrlf."""
from pathlib import Path
import hashlib,json,re,sys,zipfile
sys.path.insert(0,str(Path(__file__).resolve().parent))
import build_pack as bp,build_full as bf
ROOT=bf.ROOT
THAI=re.compile(r'[฀-๿]')

def verify():
 rp=ROOT/'resourcepacks'/bf.NAME;friends=ROOT/bf.FRIENDS
 snap=lambda:{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'config').rglob('*')) if p.is_file()}
 # 1. rebuild and compare file CONTENT inside both zips
 def content(z):
  with zipfile.ZipFile(z) as f:
   assert f.testzip() is None
   return {n:hashlib.sha256(f.read(n)).hexdigest() for n in f.namelist()}
 a=(content(rp),content(friends));bf.build();b=(content(rp),content(friends))
 assert a==b,'Non-deterministic build'
 # 2. lang: every source key present in both locales with the same text
 with zipfile.ZipFile(rp) as z:
  names=set(z.namelist());nk=0
  for d in sorted((bf.SRC/'lang').iterdir()):
   p=d/'lang/th_th.json'
   if not p.exists():continue
   src=bp.read(p)
   for loc in ('en_us','th_th'):
    got=json.loads(z.read(f'assets/{d.name}/lang/{loc}.json'));assert got==src,(d.name,loc)
   nk+=len(src)
  assert not any(n.endswith(('.ttf','.otf','.jar')) for n in names),'font/binary bundled'
  pat=[n for n in names if '/patchouli_books/' in n and n.endswith('.json')]
  npf=sum(1 for _ in (bf.SRC/"patchouli/src").rglob("*.json"));assert len(pat)==2*npf,len(pat)
  assert sum(1 for n in pat if THAI.search(z.read(n).decode('utf-8')))>=2*100
 # 3. quests round-trip from the delivered lang file
 qsrc=bp.read(bf.SRC/'quests/source.json');qt=bp.read(bf.SRC/'quests/translations.json')['items']
 for loc in ('en_us','th_th'):
  text=(ROOT/'config/ftbquests/quests/lang'/(loc+'.snbt')).read_text(encoding='utf-8')
  assert bp.parse_quest(text)==qt
  for k,v in qt.items():assert bp.special(qsrc['items'][k])==bp.special(v),k
 # 4. friends package manifest
 with zipfile.ZipFile(friends) as z:
  man=json.loads(z.read('SHA256.json'))
  for n,dg in man.items():assert hashlib.sha256(z.read(n)).hexdigest()==dg,n
  assert len(z.namelist())==len(man)+1
  for n in z.namelist():assert not n.startswith(('/','\\')) and '..' not in Path(n).parts,n
 res={'zip_crc':'PASS','deterministic_rebuild':'PASS','lang_keys':nk,"patchouli_files":npf,'quest_records':len(qt),'quest_roundtrip':'PASS','manifest':'PASS','runtime_game_test':'NOT_RUN'}
 bp.write(ROOT/'review/verification-full.json',res)
 print('PASS',res)
if __name__=='__main__':verify()
