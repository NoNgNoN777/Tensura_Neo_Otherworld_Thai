"""Build the current Thai test release with Python 3.10+, no external packages.

This is an IN_PROGRESS build; coverage is shipped alongside it, not hidden.
Run from any directory. It never edits the instance or Git index.
"""
from pathlib import Path
import collections,hashlib,json,re,shutil,tempfile,zipfile
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'translation-src'
NAME='ZZ_Tensura_Neo_Otherworld_Thai_InProgress.zip'

def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def write(path,obj):
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def parse_quest(text):
 """Consume the entire string/array-only SNBT root, with optional commas."""
 dec=json.JSONDecoder();i=0
 def ws():
  nonlocal i
  while i<len(text) and (text[i].isspace() or text[i]==','):i+=1
 def val():
  nonlocal i
  ws()
  if text[i]=='[':
   i+=1;out=[];ws()
   while text[i]!=']':out.append(val());ws()
   i+=1;return out
  value,i2=dec.raw_decode(text,i);i=i2
  if not isinstance(value,str):raise ValueError('Non-string quest language value')
  return value
 ws();assert text[i]=='{';i+=1;out={};ws()
 while text[i]!='}':
  m=re.match(r'([a-z_][a-z0-9_]*\.[^\s{}:]+)\s*:',text[i:]);assert m,repr(text[i:i+80])
  key=m[1];assert key not in out,key;i+=m.end();out[key]=val();ws()
 i+=1;ws();assert i==len(text),'Unexpected trailing SNBT'
 return out

def special(text):
 """Format-sensitive quest directives and JSON click actions must survive."""
 lines=text if isinstance(text,list) else [text];out=[]
 for line in lines:
  out.extend(re.findall(r'\{(?:image|translate):[^}]+\}',line))
  try:obj=json.loads(line)
  except (ValueError,TypeError):continue
  def walk(x):
   if isinstance(x,dict):
    for k,v in x.items():
     if k in ('clickEvent','hoverEvent'):out.append(json.dumps({k:v},sort_keys=True,ensure_ascii=False))
     else:walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(obj)
 return sorted(out)

def zip_tree(folder,dest):
 dest.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(folder.rglob('*')):
   if p.is_file():
    info=zipfile.ZipInfo(p.relative_to(folder).as_posix(),(2026,11,16,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
    z.writestr(info,p.read_bytes())
 with zipfile.ZipFile(dest) as z:assert z.testzip() is None

def build():
 coverage=read(ROOT/'review/coverage.json');entries=read(SRC/'lang-entries.json')
 assert len(entries)==coverage['lang_covered']
 # Temp directory is owned by this invocation; existing work and outputs stay intact on failure.
 with tempfile.TemporaryDirectory(prefix='thai-build-',dir=ROOT) as tmp:
  stage=Path(tmp);rp=stage/'pack';rp.mkdir();langs={};ids=set()
  for item in entries:
   assert item['id'] not in ids;ids.add(item['id'])
   assert not item['path'],'Nested component needs a component-aware builder'
   langs.setdefault(item['namespace'],{})[item['key']]=item['th']
  for ns,data in langs.items():
   for locale in ('en_us','th_th'):write(rp/'assets'/ns/'lang'/(locale+'.json'),data)
  shutil.copytree(SRC/'resourcepack',rp,dirs_exist_ok=True)
  write(rp/'pack.mcmeta',{'pack':{'pack_format':34,'description':'Tensura Neo Otherworld Thai — IN PROGRESS; English names / Thai explanations'}})
  # Detect font-reference cycles; no third-party font binaries are distributed.
  for p in (rp/'assets').glob('*/font/*.json'):
   ns=p.relative_to(rp/'assets').parts[0];own=ns+':'+p.stem
   for provider in read(p)['providers']:assert provider.get('id')!=own,'Font cycle: '+own
  deliver=stage/'player';deliver.mkdir();shutil.copytree(SRC/'config-overlay',deliver,dirs_exist_ok=True)
  qsrc=read(SRC/'quests/source.json');qt=read(SRC/'quests/translations.json')['items']
  original=(SRC/'quests/original-en_us.snbt').read_text(encoding='utf-8-sig')
  assert parse_quest(original)==qsrc['items'],'Quest source spans no longer match source'
  assert set(qt)<=set(qsrc['items'])
  for k,th in qt.items():
   en=qsrc['items'][k];assert type(th)==type(en),k
   assert special(en)==special(th),'Quest directive changed: '+k
   span=qsrc['spans'][k]
   if isinstance(en,str):assert json.loads(original[span['start']:span['end']])==en,k
  text=original
  for k,span in sorted(qsrc['spans'].items(),key=lambda pair:pair[1]['start'],reverse=True):
   if k in qt:text=text[:span['start']]+json.dumps(qt[k],ensure_ascii=False)+text[span['end']:]
  expected=dict(qsrc['items']);expected.update(qt);assert parse_quest(text)==expected
  for loc in ('en_us','th_th'):
   dest=deliver/'config/ftbquests/quests/lang'/(loc+'.snbt');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text,encoding='utf-8')
  for p in (deliver/'config/ponderer/scripts').glob('*.json'):
   data=read(p)
   def check(x):
    if isinstance(x,dict):
     if 'en_us' in x:assert 'th_th' in x and x['en_us']==x['th_th'],str(p)
     for v in x.values():check(v)
    elif isinstance(x,list):
     for v in x:check(v)
   check(data)
  zip_tree(rp,deliver/'resourcepacks'/NAME)
  shutil.copyfile(ROOT/'INSTALL_TH.md',deliver/'INSTALL_TH.md')
  write(deliver/'TRANSLATION_COVERAGE.json',coverage)
  files={p.relative_to(deliver).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(deliver.rglob('*')) if p.is_file()}
  write(deliver/'SHA256.json',files)
  # Validate all final JSON and ZIP entries before publishing artifacts.
  for p in deliver.rglob('*.json'):read(p)
  friends=stage/'Tensura_Neo_Otherworld_Thai_InProgress_For_Friends.zip';zip_tree(deliver,friends)
  for folder in ('resourcepacks','config'):
   shutil.copytree(deliver/folder,ROOT/folder,dirs_exist_ok=True)
  shutil.copyfile(friends,ROOT/friends.name)
  write(ROOT/'review/build-report.json',{'status':'PASS','release_status':coverage['status'],'files_sha256':files,'lang_keys':len(entries),'quest_records':len(qt),'quest_roundtrip':'PASS','zip_crc':'PASS','runtime_test':'NOT_RUN','hud_overlap':'UNRESOLVED'})
  print(f'Built {friends.name}; lang={len(entries)}, quest={len(qt)}; NOT a complete translation')

if __name__=='__main__':build()
