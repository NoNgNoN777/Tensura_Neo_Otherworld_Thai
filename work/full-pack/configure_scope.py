from pathlib import Path
import json,zipfile,re
w=Path(r'E:\minecratf\work\Tensura-complete');p=w/'project.json';d=json.loads(p.read_text(encoding='utf-8'));d['scope']={'lang':True,'quests':False,'puffish':False};d['override_en_us']=True;d['lang_include'] += [r'ponder',r'^(gui|message|chat)\.',r'^tensura\.(dialogue_window|researcher_menu|great_sage)',r'^ftbquests\.'];d['export_dir']=r'E:\minecratf\releases\Tensura\complete';p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
cache=json.loads((w/'cache/lang_sources.json').read_text(encoding='utf-8'));hits=[]
for ns,keys in cache['en'].items():
 for k,v in keys.items():
  if isinstance(v,str) and re.search(r'Found in dungeon chests|Obtainment|Welcome to the world|Good fortune|reincarnation.*complete',v,re.I):hits.append({'namespace':ns,'key':k,'english':v})
(w/'screenshot-source-hits.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(hits,ensure_ascii=False)[:2500])
(w/'plan.md').write_text('''# แปล Tensura ต่อให้ครบตามคำสั่งผู้ใช้
ใช้English US +คำอธิบายไทย;ชื่ออุปกรณ์/บอส/สกิลชื่อเฉพาะคงอังกฤษ
ต่อจากfriend snapshot d8c738c402รายการโดยรักษาบริบทแก้ล่าสุด
ขยายlang/Ponder/บทพูด/คู่มือ/เควสต์55หมวดและข้อความผู้เล่นKubeJSที่มีจริง
RPGรักษาอารมณ์,กลไก/เครื่องจักรไทยง่าย,placeholder/ตัวเลข/หน่วยครบ
FTB langSNBTต้องจัดการเสริมเอง ไม่ถือว่าพร้อมเพียงเพราะmttlangผ่าน
ตรวจสาเหตุอักษรซ้อนทั้งboldและตำแหน่งHUD ไม่เดาว่าเป็นปัญหาฟอนต์อย่างเดียว
เก็บต้นฉบับกับสถานะในworkนี้;ปลายทางrepoTensuraเดิม;ไม่commit/push
สร้างhandoffรีวิวหนึ่งจุดพร้อมsource,คำแปล,ข้อยกเว้น,รายงานQA,พรอมป์ต์ผู้ตรวจ
การติดตั้งหลังสร้างต้องสำรองและไม่ทับZIPที่เกมล็อก
''',encoding='utf-8')
