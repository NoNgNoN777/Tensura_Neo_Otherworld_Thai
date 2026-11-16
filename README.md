# Tensura Neo Otherworld Thai

ภาษาไทยสำหรับ Tensura Neo Otherworld 1.1.3b2 / Minecraft 1.21.1 NeoForge โดยเล่นด้วยภาษาเกม English (US) และคงชื่ออุปกรณ์/สกิลเฉพาะเป็นอังกฤษ

**ยังอยู่ระหว่างแปล ไม่ใช่ชุดสมบูรณ์** ดู [สถานะล่าสุด](TRANSLATION_STATUS.md) และ [รายการที่ต้องตรวจบริบท](review/SEMANTIC_WATCHLIST_TH.md)

- ชุดสำหรับลอง: `Tensura_Neo_Otherworld_Thai_InProgress_For_Friends.zip`
- ติดตั้งและย้อนกลับ: [INSTALL_TH.md](INSTALL_TH.md)
- ต้นฉบับ: `translation-src/` รวมภาษา Resource Pack, ฟอนต์อ้างอิง, ต้นฉบับ SNBT และคำแปล, Ponder config
- สร้าง: `python tools/build_pack.py` (Python 3.10+ ไม่ใช้แพ็กเกจภายนอก ไม่ต้องมีเกม)
- ตรวจไฟล์และความคงที่ของ build: `python tools/verify_pack.py`
- ผลตรวจและงานค้าง: `review/` ไม่ถือว่าไฟล์ ZIP สร้างผ่านแล้วแปลครบ
- พรอมป์ต์ตรวจอิสระภายหลัง: [REVIEW_PROMPT_TH.md](REVIEW_PROMPT_TH.md)

ไม่มีไฟล์ม็อดหรือฟอนต์ของผู้อื่นแนบมา ผู้เล่นต้องมีฟอนต์ไทยที่ใช้ได้อยู่แล้ว แพ็กนี้อ้างอิง default font ของเกม ยังไม่ได้ยืนยันผลในเกมกับหน้าต่างทุกชนิด

งานเดิมของผู้ร่วมแปลยังอยู่ใน `work/` และงานต่อใน `work/full-pack/` ไม่มีการ commit หรือ push อัตโนมัติ
