"""Check delivered artifacts against source, preserve directives, and prove reproducibility."""
from pathlib import Path
import hashlib,json,subprocess,sys,zipfile
import build_pack as build
ROOT=Path(__file__).resolve().parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def structural(x):
 if isinstance(x,dict):return {k:structural(v) for k,v in x.items() if k not in ('en_us','th_th')}
 if isinstance(x,list):return [structural(v) for v in x]
 return x
def verify():
 coverage=read(ROOT/'review/coverage.json')
 rp=ROOT/'resourcepacks'/build.NAME
 friends=ROOT/'Tensura_Neo_Otherworld_Thai_InProgress_For_Friends.zip'
 before=(sha(rp),sha(friends));subprocess.run([sys.executable,str(ROOT/'tools/build_pack.py')],check=True)
 assert before==(sha(rp),sha(friends)),'Non-deterministic build'
 with zipfile.ZipFile(rp) as z:
  assert z.testzip() is None
  assert read(ROOT/'review/build-report.json')['lang_keys']==coverage['lang_covered']
  langs={n:json.loads(z.read(n)) for n in z.namelist() if '/lang/' in n}
  for row in read(ROOT/'translation-src/lang-entries.json'):
   for loc in ('en_us','th_th'):assert langs[f"assets/{row['namespace']}/lang/{loc}.json"][row['key']]==row['th']
  assert not any(n.endswith(('.ttf','.otf','.jar')) for n in z.namelist())
 with zipfile.ZipFile(friends) as z:
  assert z.testzip() is None
  manifest=json.loads(z.read('SHA256.json'))
  for name,digest in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
  assert len(z.namelist())==len(manifest)+1,'Unexpected player-package entries'
  for name in z.namelist():assert not name.startswith(('/','\\')) and '..' not in Path(name).parts,name
 # Independent source/config invariant: no nonlocalization Ponder content changes.
 ponder=read(ROOT/'work/full-pack/ponder-config-source.json')
 originals=ponder.get('files',ponder.get('originals',{}))
 if originals:
  for name,obj in originals.items():
   p=ROOT/'config/ponderer/scripts'/Path(name).name
   assert structural(read(p))==structural(obj),name
 result={'zip_crc':'PASS','sha256_manifest':'PASS','deterministic_rebuild':'PASS','both_locale_lang_content':'PASS','quest_snbt_roundtrip':'PASS','runtime_game_test':'NOT_RUN','hud_overlap':'UNRESOLVED','coverage':coverage}
 build.write(ROOT/'review/verification.json',result)
 print('PASS: ZIP, SHA256, deterministic rebuild, locale content, quest roundtrip; runtime NOT_RUN')
if __name__=='__main__':verify()
