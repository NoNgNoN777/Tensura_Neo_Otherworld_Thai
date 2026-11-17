"""Remove synthetic bold/italic from translation text for the supplied Thai font.

Does not replace fonts or alter colors, placeholders, Patchouli links or resource IDs.
"""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent.parent
def clean(s):
 # Formatting codes in game text; URL values themselves are not game formatting.
 if s.startswith(('http://','https://')):return s
 return re.sub(r'\$\([lo]\)|[§&][lo]','',s)
def walk(x):
 if isinstance(x,str):return clean(x)
 if isinstance(x,list):return [walk(v) for v in x]
 if isinstance(x,dict):return {k:walk(v) for k,v in x.items()}
 return x
def main():
 src=ROOT/'translation-src'
 paths=list((src/'lang').glob('*/lang/th_th.json'))+[src/'quests/translations.json',src/'patchouli/translations.json']+list((src/'config-overlay').rglob('*.json'))
 changes=[]
 for p in paths:
  old=json.loads(p.read_text(encoding='utf-8-sig'));new=walk(old)
  if new!=old:
   p.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');changes.append(p.relative_to(ROOT).as_posix())
 (ROOT/'review/font-style-fix.json').write_text(json.dumps({'changed_files':changes,'removed_styles':['bold','italic'],'runtime_verified':False},ensure_ascii=False,indent=2),encoding='utf-8')
 print('Changed translation files:',len(changes))
if __name__=='__main__':main()
