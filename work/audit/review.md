# ตรวจคำแปลซ้ำ 10 รอบ

## ขอบเขตและผลจริง
ตรวจงานที่ทำแล้วทั้งหมด: 402 keys ของ namespace tensura (390 keys จาก batch 001–013 และ 12 จาก memory) เทียบกับ source ที่เลือกไว้ 723 keys และ JAR ต้นทางปัจจุบัน
ไม่ใช่การตรวจคำแปลทุกม็อดใน instance และไม่ใช่การรับรองว่าข้อความทุกประโยคสมบูรณ์หรือแสดงผลถูกต้องในเกม

หลังแก้ รันชุดตรวจเต็ม 10 รอบ รอบละ 10 ด้าน รวม 100 checks ผ่านทั้งหมด ผลรายรอบอยู่ใน round-01.json ถึง round-10.json และ .log ชื่อเดียวกัน SHA256 ของ ZIP ตรงกันทั้ง 10 รอบ
การตรวจซ้ำยืนยันความคงที่ของผลตรวจ ไม่ได้เพิ่มความครอบคลุมด้านความหมายสิบเท่า

## ด้านที่ตรวจในแต่ละรอบ
1. JSON UTF-8 ไม่มี BOM/duplicate keys, todo/done keys ตรงกัน, ไม่ว่าง, source ไม่เก่า
2. ต้นฉบับอังกฤษทั้ง 723 keys ตรงกับ assets/tensura/lang/en_us.json ใน JAR ต้นทาง
3. จำนวน placeholder และ brace token ของทั้ง 402 keys
4. ตัวเลขและจำนวนครั้งที่ปรากฏของทั้ง 402 keys
5. อักขระเสีย/control characters, รหัสสีและจำนวนบรรทัด
6. ศัพท์เฉพาะที่กำหนดและรายการข้อความที่ยังอังกฤษ (ตรวจศัพท์เฉพาะบางคำ ไม่ใช่การรับรองชื่อทั้งหมด)
7. ปัญหาบริบทที่พบจากการอ่านทบทวน: Inert/Inactive และ Dead End Rainbow
8. mtt validate รวมทุกคำแปล
9. ZIP CRC, สมาชิกซ้ำ, path, ไม่แนบ JAR, pack_format 34 และไม่ override en_us
10. ข้อความใน ZIP/โฟลเดอร์ build ตรงกับคำแปลทั้งหมด และจำนวนรายการ

## ก่อน–หลัง
| ประเด็น | ก่อน | หลัง | หลักฐาน |
|---|---|---|---|
| Inert | ไม่ทำงาน เช่นเดียวกับ Inactive | อยู่ระหว่างคูลดาวน์ | javap -c -p ของ CharybdisCoreBlock: SculkSensorPhase.COOLDOWN ใช้ key inert |
| Dead End Rainbow | หากเป็นไปตามเงื่อนไข... | ตามหลักแล้วจะลด... | ต้นฉบับใช้ Ideally ไม่ระบุเงื่อนไขเพิ่มเติม |
| ปัญหาบริบทตามเกณฑ์ตรวจนี้ | 2 | 0 | baseline.json เทียบ final.json รอบ 7 |
| รายการใน pack | 402 | 402 | เทียบ ZIP ก่อนและหลัง; ไม่เพิ่มขอบเขตการแปล |
| mtt errors / warnings | 0 / 2 | 0 / 2 | warnings คือยังไม่แปล 321 รายการและคงชื่อ Dwargon |

ตรวจ memory ทั้ง 12 รายการเทียบอังกฤษใน JAR แล้ว Previous/Next ของ kiln ถูกต้อง ไม่ใช่การแปลทิศทางซ้าย/ขวาตามชื่อ key
ใช้ todo_025/done_025 เป็น batch แก้บริบทของ memory 1 key เพื่อให้ build และการทำงานต่อเก็บคำแก้ไว้ ไม่แก้ memory กลางของ skill หรือ resolved.json โดยตรง
จำนวน batch จึงเพิ่มเป็น 25 โดย 025 เป็น correction ไม่ใช่งานแปลใหม่; batch หลักยังเสร็จ 13/24 และจุดเริ่มงานถัดไปยังเป็น todo_014

## ข้อจำกัด
ไม่ได้เปิดเกม/ติดตั้ง resource pack จึงยังไม่ยืนยันฟอนต์ ข้อความล้น การแสดงตัวเลข runtime และการโต้ตอบจริง
ศัพท์กลไกที่ต้นฉบับกำกวมยังต้องตรวจในเกมเมื่อถึงขั้นทดสอบ ไม่มีการเปลี่ยนสูตรหรือกลไกม็อด
ไม่ได้แก้ข้อความ 321 รายการที่ยังไม่แปล ไม่ได้ตรวจเควสต์/ส่วนเสริมที่ยังไม่มีคำแปล
พบ Python stdout encoding cp1252 ระหว่างอ่านข้อมูล จึงกำหนด stdout เป็น UTF-8 แล้วอ่านซ้ำ ไม่ได้เปลี่ยน encoding ของระบบ
git diff --check ผ่าน มีเพียงคำเตือน LF จะเปลี่ยนเป็น CRLF ตามการตั้งค่า Git

## ไฟล์และ Git
แก้ work/batches/done_001.json, work/validate.md
เพิ่ม scripts/audit_translations.py, work/batches/todo_025.json, work/batches/done_025.json และรายงาน work/audit/
build ZIP ใหม่อยู่ใน work/build/ ซึ่งถูก ignore; ไม่ install, stage, commit หรือ push

เจ้าของ repository ตรวจข้อมูลและ diff ก่อนรันเอง:
```powershell
Set-Location 'D:\Git\Tensura_Neo_Otherworld_Thai'
git status --short
git diff --check
git diff -- work/batches/done_001.json work/validate.md
git add -- scripts/audit_translations.py work/batches/done_001.json work/batches/todo_025.json work/batches/done_025.json work/validate.md work/audit
git diff --cached
git commit -m "Review Tensura translations and fix context errors"
git push origin main
```
Codex ไม่ได้รัน stage/commit/push เหล่านี้ หากนำ script ไปใช้เครื่องอื่น ให้ส่ง --tool เป็น path ของ mtt.py ที่ติดตั้งบนเครื่องนั้น
