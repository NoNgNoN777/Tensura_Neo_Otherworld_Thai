"""Snapshot reviewed/current translations into a standalone, reproducible repo layout."""
from pathlib import Path
import importlib.util,json,zipfile,re,shutil,hashlib
w=Path(__file__).resolve().parent;root=w.parent.parent
skill=root.parent/'modpack-thai-translator/scripts/mtt.py'
spec=importlib.util.spec_from_file_location('mtt',skill);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
src=json.loads((w/'source.json').read_text(encoding='utf-8'))['items'];tr=m.all_translations(str(w))
out=root/'translation-src';out.mkdir(exist_ok=True)
def put(path,data):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
entries=[];remaining=[]
def readable(s):return re.sub(r'[§&]l','',s) if re.search('[ก-๛]',s) else s
for ik,it in src.items():
 if ik not in tr:remaining.append({'id':ik,'en':it['en'],'origin':it.get('origin')});continue
 if not ik.startswith('lang|'):continue
 _,ns,_=ik.split('|',2)
 entries.append({'id':ik,'namespace':ns,'key':it['key'],'path':it.get('path',''),'en':it['en'],'th':readable(tr[ik]),'origin':it.get('origin')})
put(out/'lang-entries.json',entries)
put(root/'review/pending-lang.json',remaining)
q=json.loads((w/'quest-source.json').read_text(encoding='utf-8'));qt=json.loads((w/'quest-translations.json').read_text(encoding='utf-8'))
put(out/'quests/source.json',q);put(out/'quests/translations.json',qt)
shutil.copyfile(w/'quest-source-original.snbt',out/'quests/original-en_us.snbt')
for f in (w/'config-overlay').rglob('*.json'):
 dest=out/'config-overlay'/f.relative_to(w/'config-overlay');dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f,dest)
put(root/'review/pending-quests.json',[{'key':k,'en':v} for k,v in q['items'].items() if k not in qt['items']])
inst=Path(json.loads((w/'project.json').read_text(encoding='utf-8'))['instance'])
fonts=json.loads((w/'font-inventory.json').read_text(encoding='utf-8'));fontnotes=[]
for item in fonts:
 p=item['path']
 if p.endswith('kubejs/font/icons.json'):continue
 if '/font/mincho.json' in p or '/font/greatsage_cjk.json' in p:
  data={'providers':[{'type':'reference','id':'minecraft:default'}]};kind='route scene text through the installed default Thai font'
 elif '/beyond_gacha_c/font/' in p:
  with zipfile.ZipFile(inst/'mods'/item['jar']) as z:data=json.loads(z.read(p))
  data['providers'].append({'type':'reference','id':'minecraft:default'});kind='keep colored Latin bitmap glyphs; add default-font fallback'
 else:continue
 put(out/'resourcepack'/p,data);fontnotes.append({'path':p,'change':kind,'runtime_tested':False})
put(root/'review/font-changes.json',fontnotes)
put(root/'review/pending-manuals.json',json.loads((w/'manual-inventory.json').read_text(encoding='utf-8')))
baseline={}
for f in (out/'config-overlay/config').rglob('*'):
 if f.is_file():
  rel=f.relative_to(out/'config-overlay').as_posix();original=inst/rel
  baseline[rel]=hashlib.sha256(original.read_bytes()).hexdigest() if original.exists() else None
baseline['config/ftbquests/quests/lang/en_us.snbt']=hashlib.sha256((out/'quests/original-en_us.snbt').read_bytes()).hexdigest()
put(out/'install-baseline.json',baseline)
summary={'status':'IN_PROGRESS','minecraft':'1.21.1','pack_format':34,'lang_selected':len(src),'lang_covered':len(entries),'lang_pending':len(remaining),'quest_records_total':len(q['items']),'quest_records_covered_including_preserved_names_and_references':len(qt['items']),'quest_pending':len(q['items'])-len(qt['items']),'ponder_config_files':len(list((out/'config-overlay').rglob('*.json'))),'manual_files_pending':len(json.loads((w/'manual-inventory.json').read_text(encoding='utf-8'))),'layout_overlap_fixed':False,'font_runtime_verified':False,'committed':False}
put(root/'review/coverage.json',summary)
(root/'TRANSLATION_STATUS.md').write_text(f'''# สถานะงานแปลทั้งแพ็ก: ยังไม่ครบ

ใช้ English (US), คงชื่อเฉพาะอังกฤษ, แปลเนื้อเรื่องและคำอธิบายไทย ไม่มีการ commit/stage/push

- Lang ที่มีคำแปลหรือคงคำตามบริบท: {len(entries):,} / {len(src):,} ข้อ; ยังขาด {len(remaining):,} ข้อ
- เควส: ครอบคลุม {len(qt['items']):,} / {len(q['items']):,} ระเบียน รวมชื่อเฉพาะและตัวอ้างอิงที่คงเดิม; ยังขาด {len(q['items'])-len(qt['items']):,} ระเบียน
- Ponder ใน config: 12 ไฟล์ / 43 ข้อความ; UI ของ Ponder namespace มีคำแปลครบในขอบเขตที่เลือก
- คู่มือที่สำรวจพบและยังต้องทำ: 144 ไฟล์
- ปรับแหล่งภาษา Great Sage ตามแพ็กภายใน TNO ที่เปิดใช้อยู่ 30 ข้อ
- แก้การอ้างอิงฟอนต์ใน Resource Pack แล้ว แต่ยังไม่ได้ทดสอบในเกม; ปัญหาตำแหน่งซับทับแชตยังไม่แก้สำเร็จ

ชุดทดสอบ: `Tensura_Neo_Otherworld_Thai_InProgress_For_Friends.zip` ไม่ใช่ชุดแปลเสร็จสมบูรณ์ ยังไม่ได้ติดตั้งชุดใหม่นี้ลง instance

ต้นฉบับสำหรับสร้างซ้ำ: `translation-src/`; สร้างด้วย `python tools/build_pack.py`; ตรวจด้วย `python tools/verify_pack.py`
งานเพื่อนเดิมใน `work/` คงไว้ งานต่ออยู่ `work/full-pack/`
รายการตกหล่นทุก key อยู่ `review/pending-lang.json`, `review/pending-quests.json`, `review/pending-manuals.json`
จุดเสี่ยงความหมายและภาพ: `review/SEMANTIC_WATCHLIST_TH.md`; ผลตรวจอัตโนมัติ: `review/verification.json`
ผลตรวจอัตโนมัติผ่านไม่เท่ากับแปลครบหรือผ่านทดสอบภาพในเกม
''',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
