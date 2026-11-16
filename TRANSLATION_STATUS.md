# สถานะงานแปลทั้งแพ็ก: ยังไม่ครบ

ใช้ English (US), คงชื่อเฉพาะอังกฤษ, แปลเนื้อเรื่องและคำอธิบายไทย ไม่มีการ commit/stage/push

- Lang ที่มีคำแปลหรือคงคำตามบริบท: 1,555 / 11,217 ข้อ; ยังขาด 9,662 ข้อ
- เควส: ครอบคลุม 297 / 1,878 ระเบียน รวมชื่อเฉพาะและตัวอ้างอิงที่คงเดิม; ยังขาด 1,581 ระเบียน
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
