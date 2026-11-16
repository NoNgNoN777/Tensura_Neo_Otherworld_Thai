"""Reviewed quest-title grammar; names remain English, no prose guessing."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parent
src=json.loads((w/'quest-source.json').read_text(encoding='utf-8'))['items']
out=json.loads((w/'quest-translations.json').read_text(encoding='utf-8'))['items']
tags={'Advanced':'ขั้นสูง','Main Story':'เนื้อเรื่องหลัก','Side Quest':'เควสรอง','Artifact':'Artifact','Recycle':'แลกคืน','Tips':'คำแนะนำ','Basic Material':'วัตถุดิบพื้นฐาน'}
rules=[
 (r'Obtain the Unique Skill (.+)',lambda m:'ได้รับ Unique Skill '+m[1]),
 (r'Obtain and master (.+)',lambda m:'ได้รับและฝึก '+m[1]+' จนชำนาญ'),
 (r'Obtain (.+) and master it',lambda m:'ได้รับและฝึก '+m[1]+' จนชำนาญ'),
 (r'EP reaches ([0-9,.]+(?: million)?)',lambda m:'มี EP ถึง '+m[1].replace(' million',' ล้าน')),
 (r'Grade ([123]) Ancient Artifact',lambda m:'Ancient Artifact ระดับ '+m[1]),
 (r'(Earth|Wind|Fire|Water) Elf([·•])Low Level',lambda m:m[1]+' Elf'+m[2]+'ระดับต่ำ'),
 (r'(Earth|Wind|Fire|Water) Elf([·•])High Level',lambda m:m[1]+' Elf'+m[2]+'ระดับสูง'),
 (r'(Earth|Wind|Fire|Water) Elf([·•])Intermediate',lambda m:m[1]+' Elf'+m[2]+'ระดับกลาง'),
]
reviewed={}
for k,en in src.items():
 if k in out or not k.endswith('.title') or not isinstance(en,str):continue
 if re.fullmatch(r'\{translate:"[a-z_]+\.[A-Fa-f0-9]+\.title"\}',en):
  out[k]=en;reviewed[k]='opaque reference';continue
 # Preserve formatting but remove bold for Thai readability.
 text=re.sub(r'[&§]l','',en)
 prefix=''
 while True:
  m=re.match(r'^(?:[&§][0-9a-f]|&#[A-Fa-f0-9]{6}|【[^】]+】|\[[^\]]+\])',text)
  if not m:break
  token=m[0];text=text[len(token):]
  for a,b in tags.items():token=token.replace('【'+a+'】','【'+b+'】').replace('['+a+']','['+b+']')
  prefix+=token
 text=text.lstrip()
 if text.startswith('Ultimate Skill'):
  out[k]=prefix+text;reviewed[k]='named Ultimate Skill';continue
 for pattern,fn in rules:
  m=re.fullmatch(pattern,text)
  if m:
   out[k]=prefix+fn(m);reviewed[k]=pattern;break
(w/'quest-translations.json').write_text(json.dumps({'items':out},ensure_ascii=False,indent=2),encoding='utf-8')
(w/'quest-template-review.json').write_text(json.dumps(reviewed,ensure_ascii=False,indent=2),encoding='utf-8')
print('New template/name/reference records:',len(reviewed),'Total quest records:',len(out))
