from pathlib import Path
import json,re
w=Path(r'E:\minecratf\minecratf_repo_git\Tensura_Neo_Otherworld_Thai\work\full-pack');rows=json.loads((w/'quest-chapter-index.json').read_text(encoding='utf-8'));translations={};generic={
0:'ชีวิตคนเหมืองยามค่ำคืน',5:'【มิติ】อาณาจักรของเหล่า Elf',16:'【มิติ】ดินแดนที่ Devil อาศัยอยู่',17:'นักชิมจากต่างโลก',18:'การผจญภัยในต่างโลกของฉัน',21:'【การอธิษฐาน】วิหาร Elven Garden',22:'【พ่อค้า】ร้านของ Dwarf',23:'ภารกิจกำจัดภัยพิบัติของกิลด์',24:'【ผจญภัย】การเดินทางอันน่าประทับใจ',25:'【เนื้อเรื่องหลัก】เรื่องเล่าจากต่างโลก',26:'กลไกการเล่น',29:'【สกิล】เวทมนตร์ก็คือวิทยาศาสตร์',30:'ตำนานมังกร',31:'ดินแดนใต้ม่านสนธยา',33:'บทแห่งการเริ่มต้นสีมุก [เนื้อหายังไม่เสร็จ]',34:'【ภารกิจ】ภารกิจกิลด์นักผจญภัย',35:'ยินดีต้อนรับสู่ Reincarnation: New Otherworld',37:'【ดันเจี้ยน】เกมดันเจี้ยน [เนื้อหายังไม่เสร็จ]',42:'กาลเวลาแปรปรวน',47:"Nature's Aura",49:'แสงดาวนิรันดร์และสนธยาอันไม่สิ้นสุด',58:'【การกลับชาติมาเกิด】ล็อกสกิลและรับ Unique Skill ใหม่'}
for i,(k,en) in enumerate(rows):
 if i==53:translations[k]=en;continue
 s=re.sub(r'[&§]l','',en)
 if i in generic:
  colors=''.join(re.findall(r'[&§][0-9a-f]',s));translations[k]=colors+generic[i]
 else:
  translations[k]=s.replace('Path of Evolution','เส้นทางวิวัฒนาการ').replace('Evolution Path','เส้นทางวิวัฒนาการ')
assert len(translations)==59
(w/'quest-translations.json').write_text(json.dumps({'items':translations},ensure_ascii=False,indent=2),encoding='utf-8')
print('Quest chapter title records',len(translations),'technical reference retained 1')
