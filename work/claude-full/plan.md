# แผนแปลภาษาไทย: Tensura Neo Otherworld 1.1.3b2

ผู้ใช้อนุมัติแผนนี้ในแชทเมื่อ 2026-11-17 ("เริ่มเลย") Claude ทำคนเดียว ไม่แบ่งงานให้ AI อื่น ไม่ commit/push

## ข้อมูลแพ็ก
- Minecraft 1.21.1 / NeoForge, ม็อด 265 ไฟล์, lang namespaces 195
- instance: D:\game2\Instances\Tensura Neo Otherworld
- work: D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full   pack_id: tensura_neo_otherworld
- repo ปลายทาง: D:\minecraft\Tensura_Neo_Otherworld_Thai (วิธีเดียวกับ repo Prominence_-IIthai)

## ขอบเขต (ตามคำตอบผู้ใช้)
- lang: ตัวกรองเดียวกับ work/full-pack (คำอธิบาย, tooltip, UI, Ponder, ftbquests, greatsage, tensura) ตัด advancements, death.attack, subtitles, config, keybind
- ซับ/ข้อความ Great Sage voice: แปล · เสียงพากย์: ไม่ทำ
- เควส FTB (lang SNBT แบบใหม่ 55 บท): แปล ด้วย tools/build_pack.py ของ repo (mtt ยังไม่รองรับ)
- ชื่อไอเทม/บอส/สกิล/เผ่า/มิติ: คงอังกฤษ · ชื่อเควส: `ชื่อไทย (English)`
- คู่มือ Patchouli 144 ไฟล์, Ponderer config 12 ไฟล์, wiki ของแพ็ก: แปล
- การส่งแพ็ก: resourcepacks + config overlay · ฟอนต์: ไม่แนบ (ผู้ใช้ใส่เอง) · เซิร์ฟเวอร์: ไม่ทำ

## ตัวเลข
| ส่วน | ทั้งหมด | จาก memory/ของเดิม | ต้องแปล |
|---|---|---|---|
| lang | 11,217 | 1,537 | 9,680 |
| quest (ระเบียน SNBT) | 1,878 | 297 | 1,581 |
| คู่มือ Patchouli | 144 ไฟล์ | 0 | 144 ไฟล์ |
- lang: 128 batch (ต้นฉบับ ~1 ล้านตัวอักษร) · เควส ~125,000 ตัวอักษร

## ความเสี่ยงที่เจอจาก scan
- ต้นฉบับ Great Sage 30 ข้อมาจากแพ็กภายใน mod/tensura_tno:resourcepacks/greatsage_patches (ใช้ apply_builtin_sources.py ทุกครั้งหลัง extract)
- instance ใหม่ยังไม่มี options.txt ยืนยันการเปิด greatsage_patches ไม่ได้ ยึดตาม instance เดิม
- span ของเควสอ้างอิงไฟล์ CRLF → ต้องแก้ build ให้รับ LF ได้
- คีย์ซ้ำข้าม jar 66 คีย์ · KubeJS en_us 3 ม็อด (ชื่อไบโอม/บอส คงอังกฤษ)
- ซับไตเติลทับแชทเป็นปัญหาตำแหน่งวาด อาจแก้ด้วยแพ็กภาษาไม่ได้

## ขั้นตอน
1. แปล lang batch 001–128 (validate ทุก batch) เรียง: tensura/greatsage → ftbquests/ponder → wiki → ม็อดอื่น
2. แปลเควส 1,581 ระเบียน → translation-src/quests/translations.json
3. แปลคู่มือ Patchouli + ตรวจ macro/link
4. ตรวจความหมายซ้ำ 2 รอบ (review-*-findings.md / fixes.json)
5. build + validate + verify_pack (แก้ CRLF และให้เทียบเนื้อหาใน ZIP)
6. install ลงเกม (สำรองอัตโนมัติ) - ขออนุญาตก่อน
7. ผู้ใช้ทดสอบในเกม
8. export + harvest + อัปเดต skill modpack-thai-translator

## สิ่งที่ต้องให้ผู้ใช้ทำเอง
- ปิดเกมก่อน install, ใส่ฟอนต์ไทยเอง, เปิด resource pack, ทดสอบตาม checklist, commit/push ใน Sourcetree
