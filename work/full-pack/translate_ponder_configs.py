from pathlib import Path
import json,copy
w=Path(r'E:\minecratf\minecratf_repo_git\Tensura_Neo_Otherworld_Thai\work\full-pack');d=json.loads((w/'ponder-config-source.json').read_text(encoding='utf-8'));ths='''แนะนำ Alchemy Furnace
วางวัตถุดิบปรุงยาตามตำแหน่งที่แสดง หากมีเอฟเฟกต์เปลวไฟ แสดงว่ากำลังปรุงยา
ใช้ The Supreme Alchemy Canon หรือ Essence Charcoal เพื่อเพิ่มความเร็วในการปรุงยา
Battlewill Manual: หาจากดันเจี้ยนและเรียนสกิล
วิธีหาและคำแนะนำเบื้องต้น
มีโอกาส 50% ที่จะพบในหีบดันเจี้ยน
วิธีใช้เพื่อเรียนสกิล Battlewill
กดคลิกขวาค้างเพื่อใช้ แล้วสุ่มเรียนสกิล Battlewill หนึ่งอย่าง
เรียน Hazy Style Fighting สำเร็จแล้ว!
ที่นี่คือสมุดเควสต์หรือเปล่า?
Rimuru!
เฮ้ สวัสดี ผู้กลับชาติมาเกิด!
แนะนำ Charybdis Core
สิ่งปลูกสร้างใต้ดิน
แกนรูปร่างคล้ายไข่ ใช้อัญเชิญ Charybdis
ชาร์จครบ 100K EP เพื่อเปิดใช้งาน จากนั้นใช้รับ EP หรือคลิกขวาเพื่ออัญเชิญบอส
วิธีใช้ Kiln
แนะนำหน้าจอใช้งาน
ตัวอย่างการใช้ Magic Ore Shard
วิธีที่ 1: เปิดประตูสู่ Twilight Forest
โยน Magic Ore Shard ลงน้ำ
วิธีใช้ Mining Station
ฉากที่ 1
คลิกขวาเพื่อเปิดแล้วใส่บล็อกแร่ ไม่รับไอเทมโลหะดิบ
พิธีอัญเชิญ Feldway
พิธีอัญเชิญ Feldway
คลิกขวาที่ Mithril Block เพื่ออัญเชิญ Feldway
(ใช้ได้เฉพาะมิติ Paths Gate)
ฉากใหม่: orb_of_prophec
ฉากที่ 1
แก้ไขฉาก Ponder นี้!
ฉากใหม่: orb_of_prophecy
ฉากที่ 1
คลิกขวาที่กรอบประตูเพื่อเปิดประตูเข้าสู่มิติ
วิธีใช้ Smithing Bench
หน้าที่ของ Blueprint
ก่อนคราฟต์ที่นี่ ต้องใช้ Blueprint ปลดล็อกสูตรก่อน รับ Blueprint ได้เมื่อได้รับวัตถุดิบบางชนิด
วิธีใช้ Tom's Simple Storage
ส่วนหลัก หีบ และ Terminal
วาง Inventory Proxy ซึ่งเป็นศูนย์กลางเครือข่าย
วางหีบติดกับส่วนหลัก หีบจะเชื่อมเข้าเครือข่ายอัตโนมัติ
กดย่อพร้อมคลิกขวาที่ส่วนหลักเพื่อติดตั้ง Storage Terminal
คลิกขวาที่ Storage Terminal เพื่อเปิดดูช่องเก็บของทั้งหมดรวมกัน'''.splitlines();assert len(ths)==len(d['items'])
files=copy.deepcopy(d['files']);records=[]
for row,th in zip(d['items'],ths):
 x=files[row['file']]
 for key in row['path'][:-1]:x=x[key]
 records.append({**row,'thai':th,'used_alternate_locale_due_to_truncation':row['english'].endswith((' ing','increa',' Co','summon','100K',' Blo','to '))})
 x['en_us']=th;x['th_th']=th
out=w/'config-overlay'
for rel,data in files.items():p=out/Path(rel);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(w/'ponder-config-translations.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
# All non-locale fields must be byte-equivalent after JSON parsing.
def strip(x):
 if isinstance(x,dict):return {k:strip(v) for k,v in x.items() if k not in ('en_us','th_th')}
 if isinstance(x,list):return [strip(v) for v in x]
 return x
for rel,original in d['files'].items():assert strip(original)==strip(files[rel]),rel
print('Ponder config overlay authored:12files,43strings;structural invariants passed')
