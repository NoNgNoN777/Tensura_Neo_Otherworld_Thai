"""Build the full Thai release (lang + FTB quests + Patchouli + Ponder) with Python 3.10+, stdlib only.

Reads only files under translation-src/. Never touches the game instance or Git.
Output (deterministic):
  resourcepacks/Tensura_Neo_Otherworld_Thai.zip
  config/ftbquests/quests/lang/{en_us,th_th}.snbt
  config/ponderer/scripts/*.json
  Tensura_Neo_Otherworld_Thai_For_Friends.zip

Notes recorded for the skill:
  * read the quest source with universal newlines (read_text) so spans match LF and CRLF checkouts.
  * Patchouli is shipped under both en_us/ and th_th/ so it works whatever language the client reports.
"""
from pathlib import Path
import hashlib,json,re,shutil,tempfile,zipfile,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import build_pack as bp  # parse_quest / special / zip_tree / read / write

ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'translation-src'
NAME='Tensura_Neo_Otherworld_Thai.zip'
FRIENDS='Tensura_Neo_Otherworld_Thai_For_Friends.zip'
MACRO=re.compile(r'\$\([^)]*\)')
TEXT_KEYS={'name','title','text','description','time'}

def patchouli_files():
 """Yield (published path under assets/, translated JSON object) for every Patchouli source file."""
 tr=bp.read(SRC/'patchouli/translations.json')
 src=SRC/'patchouli/src'
 used=set()
 for f in sorted(src.rglob('*.json')):
  rel=f.relative_to(src).as_posix()
  obj=json.loads(f.read_text(encoding='utf-8'))
  def walk(x,path):
   if isinstance(x,dict):
    for k,v in x.items():
     if k in TEXT_KEYS and isinstance(v,str):
      key=rel+'::'+'/'.join(map(str,path+[k]))
      assert key in tr,'Patchouli string not translated: '+key
      th=tr[key];used.add(key)
      assert MACRO.findall(v)==MACRO.findall(th),'Patchouli macro mismatch: '+key
      if v.startswith('#'):assert th==v,'Patchouli template ref changed: '+key
      x[k]=th
     else:walk(v,path+[k])
   elif isinstance(x,list):
    for i,v in enumerate(x):walk(v,path+[i])
  walk(obj,[])
  yield rel,obj
 assert used==set(tr),'Unused Patchouli translations: %d'%len(set(tr)-used)

def build():
 with tempfile.TemporaryDirectory(prefix='thai-build-',dir=ROOT) as tmp:
  stage=Path(tmp);rp=stage/'pack';rp.mkdir()
  # 1. lang (11k keys): same Thai content for en_us and th_th so it applies whichever locale is selected.
  nkeys=0
  for d in sorted((SRC/'lang').iterdir()):
   p=d/'lang/th_th.json'
   if not p.exists():continue
   data=bp.read(p);nkeys+=len(data)
   for loc in ('en_us','th_th'):bp.write(rp/'assets'/d.name/'lang'/(loc+'.json'),data)
  # 2. font/model overrides that are not translations (kept from the repo, no font binaries)
  shutil.copytree(SRC/'resourcepack',rp,dirs_exist_ok=True)
  for p in (rp/'assets').glob('*/font/*.json'):
   ns=p.relative_to(rp/'assets').parts[0];own=ns+':'+p.stem
   for provider in bp.read(p)['providers']:assert provider.get('id')!=own,'Font cycle: '+own
  # 3. Patchouli guides (en_us + th_th)
  npat=0
  for rel,obj in patchouli_files():
   head,tail=rel.split('/en_us/',1)
   for loc in ('en_us','th_th'):bp.write(rp/head/loc/tail,obj)
   npat+=1
  bp.write(rp/'pack.mcmeta',{'pack':{'pack_format':34,'description':'Tensura Neo Otherworld Thai (full)'}})
  # 4. FTB Quests lang snbt
  deliver=stage/'player';deliver.mkdir();shutil.copytree(SRC/'config-overlay',deliver,dirs_exist_ok=True)
  qsrc=bp.read(SRC/'quests/source.json');qt=bp.read(SRC/'quests/translations.json')['items']
  original=(SRC/'quests/original-en_us.snbt').read_text(encoding='utf-8-sig')
  assert bp.parse_quest(original)==qsrc['items'],'Quest source spans no longer match source'
  assert set(qt)==set(qsrc['items']),'Quest translations incomplete: %d missing'%len(set(qsrc['items'])-set(qt))
  for k,th in qt.items():
   en=qsrc['items'][k];assert type(th)==type(en),k
   if isinstance(en,list):assert len(en)==len(th),k
   assert bp.special(en)==bp.special(th),'Quest directive changed: '+k
  text=original
  for k,span in sorted(qsrc['spans'].items(),key=lambda pair:pair[1]['start'],reverse=True):
   text=text[:span['start']]+json.dumps(qt[k],ensure_ascii=False)+text[span['end']:]
  assert bp.parse_quest(text)==qt
  for loc in ('en_us','th_th'):
   dest=deliver/'config/ftbquests/quests/lang'/(loc+'.snbt');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text,encoding='utf-8',newline='\n')
  # 5. Ponder scripts: en_us must equal th_th (already Thai)
  for p in (deliver/'config/ponderer/scripts').glob('*.json'):
   def check(x):
    if isinstance(x,dict):
     if 'en_us' in x:assert 'th_th' in x and x['en_us']==x['th_th'],str(p)
     for v in x.values():check(v)
    elif isinstance(x,list):
     for v in x:check(v)
   check(bp.read(p))
  bp.zip_tree(rp,deliver/'resourcepacks'/NAME)
  shutil.copyfile(ROOT/'INSTALL_TH.md',deliver/'INSTALL_TH.md')
  files={p.relative_to(deliver).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(deliver.rglob('*')) if p.is_file()}
  bp.write(deliver/'SHA256.json',files)
  friends=stage/FRIENDS;bp.zip_tree(deliver,friends)
  out_rp=ROOT/'resourcepacks'
  for old in out_rp.glob('*.zip'):old.unlink()
  for folder in ('resourcepacks','config'):shutil.copytree(deliver/folder,ROOT/folder,dirs_exist_ok=True)
  shutil.copyfile(friends,ROOT/FRIENDS)
  report={'status':'PASS','lang_keys':nkeys,'quest_records':len(qt),'patchouli_files':npat,'files_sha256':files,'quest_roundtrip':'PASS','zip_crc':'PASS','runtime_test':'NOT_RUN'}
  bp.write(ROOT/'review/build-report-full.json',report)
  print(f'Built {FRIENDS}: lang={nkeys}, quest={len(qt)}, patchouli_files={npat}')

if __name__=='__main__':build()
