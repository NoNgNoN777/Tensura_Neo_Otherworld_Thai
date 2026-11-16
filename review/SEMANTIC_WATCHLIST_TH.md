# จุดที่ต้องตรวจความหมายและภาพจริงต่อ

- Great Sage: ใช้ต้นฉบับจากแพ็กภายในที่เปิดอยู่ `mod/tensura_tno:resourcepacks/greatsage_patches` ไม่ใช้ข้อความระบบฝึกสุ่มเดิม ผลต่าง 30 ข้ออยู่ใน `work/full-pack/builtin-source-changes.json` ห้ามรัน scan/extract แล้วลืมใช้ `apply_builtin_sources.py` ก่อนตัดสินว่าคำแปลเก่าใช้ได้
- ภาพซับทับแชต: ยังไม่แก้สำเร็จ พบ renderer `Subtitles` และ `WorldVoiceOverlay` ใน Great Sage แต่ไม่พบตัวตั้งตำแหน่งซับใน config ที่ติดตั้ง ห้ามกล่าวว่าการแก้ default-font fallback แก้ตำแหน่งหน้าต่างแล้ว
- ฟอนต์ฉาก: `greatsage:mincho` และ `tensura_tno:greatsage_cjk` อ้างอิง `minecraft:default` เพื่อใช้ฟอนต์ไทยที่ผู้เล่นเปิดอยู่ ต้องทดสอบขนาด บรรทัด และตัวอักษรวรรณยุกต์จริง ส่วนฟอนต์สีของ Beyond Adventures คง bitmap Latin เดิมและเพิ่ม fallback เท่านั้น ไม่ได้แนบไฟล์ฟอนต์ผู้อื่น
- เควส `quest.01A2A02A26E4E44E.quest_subtitle`: ต้นฉบับอังกฤษ “Choose one of the two and Wind Manipulation” กำกวม ควรเทียบข้อความจีนหรือกลไกก่อนสรุปว่าห้ามมีทั้งสองอย่าง
- เควส `quest.07E64C0B306DB76F.quest_desc`: บรรทัด “all that apply Resistance Evolution is invalid” ผิดไวยากรณ์ในต้นฉบับ ต้องตรวจ upstream/โค้ด ไม่แต่งเป็นโบนัสหรือข้อจำกัดใหม่
- ชื่อต้นฉบับ Luminous / Lumisdin และ Wisdom King / King of Wisdom ต่างกันระหว่างเควส คงตามแต่ละข้อความ ยังไม่ได้ยืนยันว่าเป็น alias เดียวกัน
- คำเตือน validator ของ `heat_wave.description` และ `icicle_spear.description`: ต้นฉบับเป็นคำบรรยายสามัญตัวพิมพ์เล็ก (“a ... fire storm”, “a giant icicle spike”) จึงแปลเป็นพายุไฟ/หนามน้ำแข็ง ไม่ควรเปลี่ยนเป็นชื่อไอเทมอัตโนมัติเพียงเพราะชนกับชื่อในพจนานุกรม
- การนับ coverage เควสรวมชื่อเฉพาะและ `{translate:...}` ที่ตั้งใจคงเดิม ไม่ใช่จำนวนข้อความที่แปลไทยทั้งหมด
- รายการ pending มีทั้งข้อความผู้เล่น คู่มือ และ UI เครื่องมือแก้ฉาก ต้องแยกประเภทโดยตรวจบริบท ห้ามซ่อนรายการแล้วประกาศว่าแปลครบ
