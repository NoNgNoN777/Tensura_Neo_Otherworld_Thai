from pathlib import Path
import json,re,zipfile,collections
w=Path(r'E:\minecratf\minecratf_repo_git\Tensura_Neo_Otherworld_Thai\work\full-pack');inst=Path(r'D:\minecraft\Instances\Tensura Neo Otherworld');p=inst/'config/ftbquests/quests/lang/en_us.snbt';s=p.read_text(encoding='utf-8-sig');dec=json.JSONDecoder();pos=0;entries={};spans={}
def value_at(i):
 while s[i].isspace():i+=1
 if s[i]=='[':
  a=[];i+=1
  while True:
   while s[i].isspace() or s[i]==',':i+=1
   if s[i]==']':return a,i+1
   v,i=value_at(i);a.append(v)
 return dec.raw_decode(s,i)
# FTB language root is a map of string/string-array values; preserve all IDs and original spans.
for m in re.finditer(r'(?m)^\s*([a-z_][a-z0-9_]*\.[^\s{}:]+):\s*',s):
 start=m.end()
 try:v,end=value_at(start)
 except json.JSONDecodeError as e:raise RuntimeError(f'Unsupported quest value at {m.group(1)}: {e}')
 assert isinstance(v,str) or (isinstance(v,list) and all(isinstance(x,str) for x in v)),m.group(1)
 entries[m.group(1)]=v;spans[m.group(1)]={'start':start,'end':end}
(w/'quest-source.json').write_text(json.dumps({'source_path':str(p),'items':entries,'spans':spans},ensure_ascii=False,indent=2),encoding='utf-8');(w/'quest-source-original.snbt').write_bytes(p.read_bytes())
print('Quest language entries:',len(entries),'chapter titles:',sum(k.startswith('chapter.') and k.endswith('.title') for k in entries))
# Identify manual content, font declarations and the two pictured messages without editing the instance.
manual=[];font=[];hits=[]
for jar in (inst/'mods').glob('*.jar'):
 with zipfile.ZipFile(jar) as z:
  for n in z.namelist():
   if re.search(r'(patchouli_books/.*/en_us/|/ae2guide/).*\.(md|json)$',n):manual.append({'jar':jar.name,'path':n})
   if '/font/' in n and n.endswith('.json'):font.append({'jar':jar.name,'path':n})
(w/'manual-inventory.json').write_text(json.dumps(manual,ensure_ascii=False,indent=2),encoding='utf-8');(w/'font-inventory.json').write_text(json.dumps(font,ensure_ascii=False,indent=2),encoding='utf-8')
cache=json.loads((w/'cache/lang_sources.json').read_text(encoding='utf-8'))['en']
for ns,keys in cache.items():
 for k,v in keys.items():
  if isinstance(v,str) and (('50%' in v and 'chest' in v.lower()) or 'good fortune' in v.lower() or ('reincarnation' in v.lower() and 'complete' in v.lower())):hits.append({'namespace':ns,'key':k,'english':v})
(w/'screenshot-targets.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2),encoding='utf-8');print('Manual files',len(manual),'font declarations',len(font));print(json.dumps(hits,ensure_ascii=False)[:1500])
