from pathlib import Path
import json
w=Path(r'E:\minecratf\minecratf_repo_git\Tensura_Neo_Otherworld_Thai\work\full-pack');s=json.loads((w/'source.json').read_text(encoding='utf-8'))['items'];r=json.loads((w/'resolved.json').read_text(encoding='utf-8'));rows=[{'key':k,'en':v['en']} for k,v in s.items() if k.startswith('lang|tensura|') and k not in r];(w/'tensura-core-pending.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');print('CORE',len(rows))
for i,x in enumerate(rows[:100]):print(i,x['key'].split('|')[2],repr(x['en']))
