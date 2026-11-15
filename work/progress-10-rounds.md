# ผลแปล 10 รอบ

นับรอบที่ผู้ใช้ขอเพิ่มเป็น batch 004–013 รวม 300 รายการ (30 ต่อรอบ) และทำ batch 002–003 อีก 60 รายการก่อนรับคำสั่ง 10 รอบ

ก่อน 10 รอบ: 3/24 batches, build 102 รายการ
หลัง 10 รอบ: 13/24 batches, build 402 รายการ (390 จาก batch และ 12 จาก memory); เหลือ 321 จาก source 723 รายการ

## ผลตรวจ
- validate แต่ละ batch 004–013: errors 0; แก้คำเตือนชื่อ Stellar Gold coin และ Gold coin ใน 006 แล้ว
- validate รวมหลังแก้: errors 0, warnings 2 (ยังไม่แปล 321 รายการ และคงชื่อเฉพาะ Dwargon)
- build สำเร็จ; ตรวจ ZIP CRC, pack.mcmeta, keys/ตัวเลขครบ 390 รายการ และคำแปลใน ZIP ตรงกับ done files
- การตรวจตัวเลขรอบแรกพบ 3rd แปลเป็นคำว่า สาม จึงเปลี่ยนเป็น บุคคลที่ 3 และตรวจซ้ำผ่าน
- ไม่ได้ทดสอบในเกม ไม่ install ไม่ commit/push
- ศัพท์/กลไกที่กำกวมควรตรวจในเกมต่อ เช่น EP, Battlewill, Reset Counter และชื่อเผ่าพันธุ์

## ทำต่อ
เริ่ม todo_014.json แล้ว validate ก่อนขึ้น batch ถัดไป ขอบเขตรวมยังไม่เสร็จ

## ขั้นตอน Git สำหรับเจ้าของ repository
ตรวจ diff ของ work/validate.md และไฟล์ใหม่ done_002.json ถึง done_013.json รวมถึงรายงานนี้ก่อน stage
อย่าใช้ git add . โดยไม่ตรวจไฟล์ที่มี path ส่วนตัวหรือ build/backup

```powershell
Set-Location 'D:\Git\Tensura_Neo_Otherworld_Thai'
git status --short
git diff --check
git add -- work/batches/done_002.json work/batches/done_003.json work/batches/done_004.json work/batches/done_005.json work/batches/done_006.json work/batches/done_007.json work/batches/done_008.json work/batches/done_009.json work/batches/done_010.json work/batches/done_011.json work/batches/done_012.json work/batches/done_013.json work/validate.md work/progress-10-rounds.md
git diff --cached --stat
git diff --cached
# เมื่อเจ้าของตรวจแล้วจึงดำเนินการเอง:
git commit -m "Translate Tensura batches 002 through 013"
git push origin main
```

Codex ไม่ได้รันคำสั่ง stage/commit/push ข้างต้น
