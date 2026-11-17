# สถานะงานแปลทั้งแพ็ก: แปลครบแล้วสำหรับ 1.1.3c (รอทดสอบในเกม)

ตรงกับแพ็ก Tensura Neo Otherworld **1.1.3c** (อัปเดตจากชุด 1.1.3b2 เมื่อ 2026-11-17: lang +180/-36/เปลี่ยน 40, เควส เพิ่ม 18/ลบ 376/เปลี่ยน 450, Patchouli +6 ไฟล์) ใช้กับ 1.1.3b2 ไม่ได้แล้ว

ภาษาที่ใช้ English (US) คงชื่อเฉพาะเป็นอังกฤษ แปลเนื้อเรื่องและคำอธิบายเป็นไทย ไม่มีการ commit/stage/push

| ส่วน | จำนวน | สถานะ |
|---|---|---|
| lang (ทุกม็อดในแพ็ก) | 11,361 ข้อ | ครบ แปลหรือคงคำตามบริบท |
| เควส FTB | 1,520 ระเบียน | ครบ (ชื่อเควสรูป `ชื่อไทย (English)`) |
| คู่มือ Patchouli | 150 ไฟล์ / 619 ข้อความ | ครบ |
| Ponder | 12 ไฟล์ / 43 ข้อความ | ครบ (ทำไว้ก่อนหน้า) |
| ซับ Great Sage | 30 ข้อ ตามแพ็กภายใน TNO | ครบ ใช้ข้อความอังกฤษของแพ็กที่เปิดใช้อยู่ |

ตั้งใจไม่แปล: advancements (คงอังกฤษ), เสียงพากย์, ชื่อไอเทม/ม็อบ/สกิล/เผ่า/มิติ, ข้อความภาษาญี่ปุ่นในหน้าจอพิธี Great Sage (kanji)

ชุดส่งมอบ: `Tensura_Neo_Otherworld_Thai_For_Friends.zip` และ `resourcepacks/Tensura_Neo_Otherworld_Thai.zip`
สร้างซ้ำ: `python tools/build_full.py` · ตรวจ: `python tools/verify_full.py` (ผลใน `review/verification-full.json` และ `review/build-report-full.json`)

ยังไม่ทำ / ยังไม่ยืนยัน: ทดสอบในเกมจริง (ฟอนต์ไทยกับทุกหน้าต่าง, ตัดบรรทัดในเควสยาว, การแสดงผล Patchouli) และปัญหาซับ Great Sage ทับแชต

ต้นฉบับ: `translation-src/` (`lang/`, `quests/`, `patchouli/`, `config-overlay/`, `resourcepack/`) งานระหว่างทางอยู่ใน `work/claude-full/` (1.1.3b2) และ `work/v113c/` (อัปเดต 1.1.3c) สคริปต์เก่า `tools/build_pack.py` และ `tools/verify_pack.py` ยังคงไว้เป็นของชุดทดสอบเดิม (`build_full.py` เรียกใช้ฟังก์ชันของ `build_pack.py`)
