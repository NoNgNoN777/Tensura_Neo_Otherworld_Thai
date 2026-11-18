# Tensura Neo Otherworld ภาษาไทย

ชุดภาษาไทยสำหรับ **Tensura Neo Otherworld 1.1.3c** บน Minecraft Java **1.21.1 · NeoForge** อ่านเควส คำอธิบายสกิล และคู่มือเป็นไทย โดยยังค้นชื่อไอเทม ม็อบ และสกิลด้วยชื่ออังกฤษได้

**[⬇ ดาวน์โหลดชุดภาษาไทยสำหรับผู้เล่น (.zip)](https://github.com/NoNgNoN777/Tensura_Neo_Otherworld_Thai/raw/refs/heads/main/Tensura_Neo_Otherworld_Thai_For_Friends.zip)** · [คู่มือติดตั้งและย้อนกลับ](INSTALL_TH.md) · [สถานะงานแปล](TRANSLATION_STATUS.md)

## วิธีติดตั้ง

1. ปิดเกม แล้วเปิดโฟลเดอร์ instance ของ **Tensura Neo Otherworld 1.1.3c** ที่มี `mods` และ `config` สำรองไฟล์ภาษาเควสและสคริปต์ Ponder ตาม [คู่มือติดตั้ง](INSTALL_TH.md)
2. แตก ZIP ที่ดาวน์โหลด แล้วคัดลอก **ทั้ง `config` และ `resourcepacks`** ลงใน instance เดิม ให้โฟลเดอร์รวมกับของเดิม เก็บไฟล์ ZIP ที่อยู่ข้างใน `resourcepacks` ไว้ทั้งไฟล์
3. เปิดเกม เลือก **Options → Language → English (US)** จากนั้นไปที่ **Resource Packs** เปิด `Tensura_Neo_Otherworld_Thai.zip` และจัดไว้เหนือแพ็กภาษาอื่น หากใช้แพ็กฟอนต์ไทย ให้เปิดฟอนต์ของคุณด้วย

## ข้างในมีอะไร

| ส่วนของเกม | เนื้อหาในชุดแจก |
| --- | --- |
| สกิล เผ่า และหน้าจอม็อด | ข้อความภาษา 15,025 คีย์ รวมคำอธิบายสกิล แจ้งเตือนคูลดาวน์ บาเรียร์ และซับ Great Sage |
| สมุดเควส FTB Quests | ข้อมูลภาษา 1,520 ระเบียน รวมชื่อเควสและคำอธิบาย |
| หนังสือ Patchouli | คู่มือ 150 ไฟล์ รวม 619 ข้อความ |
| ฉากสาธิต Ponder | 12 ไฟล์ รวม 43 ข้อความ |

**ตัวอย่างจากแพ็ก** · เควส *Kill Yuuki* แสดงเป็น “สังหาร Yuuki” และเมื่อใช้สกิลตอนมาจิคูลหมด ข้อความ *Out of Magicule.* แสดงเป็น “มาจิคูลหมด”

## ถ้าเข้าเกมแล้วเจอภาษาอังกฤษ

- **เมนูเป็นไทย แต่เควสหรือ Ponder ยังเป็นอังกฤษ** — ปิดเกม ตรวจว่าได้คัดลอก `config` ลงใน instance ที่เปิดเล่น แล้วเปิดเกมใหม่
- **ชื่อไอเทม สกิล เผ่า และ advancements** — ชุดนี้ตั้งใจคงอังกฤษ บางข้อความของ Nirvana, FTB และปุ่มในหนังสือ Patchouli ก็ยังรอแปล
- **ตัวอักษรไทยหรือซับ Great Sage แสดงผิดตำแหน่ง** — ชุดแจกผ่านการตรวจไฟล์แล้ว การแสดงฟอนต์ การตัดบรรทัด และซับทับแชตยังรอตรวจในเกม หากพบปัญหา แนบภาพหน้าจอ ชื่อสกิลหรือเควส และเวอร์ชันม็อดแพ็กได้ที่ [Issues](https://github.com/NoNgNoN777/Tensura_Neo_Otherworld_Thai/issues)

<details>
<summary>สำหรับผู้ร่วมแปลและผู้ที่ต้องการสร้าง ZIP เอง</summary>

ต้นฉบับอยู่ใน [translation-src/](translation-src/) ใช้ Python 3.10 ขึ้นไป รันจากโฟลเดอร์หลักของ repo

```sh
python tools/build_full.py
python tools/verify_full.py
```

ผลตรวจอยู่ใน [verification-full.json](review/verification-full.json) และ [build-report-full.json](review/build-report-full.json) ส่วน [work/](work/) เก็บงานแปลระหว่างทางและข้อมูลของเวอร์ชันก่อน

</details>
