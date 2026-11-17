import sys
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp')
from gt import run
S='tensura.skill.'
D={
S+'mode_learning.no_learn':"โหมด %s ของ %s ใช้ได้โดยไม่ต้องเรียนรู้",
S+'mode_learning.no_learn_all':"ทุกโหมดของ %s ใช้ได้โดยไม่ต้องเรียนรู้",
S+'mode_learning.no_mode':"%s ไม่มีโหมด %s",
S+'mode_learning.success':"ตั้งแต้มเรียนรู้ในโหมด %s ของ %s เป็น %s สำหรับ %s แล้ว",
S+'mode_learning.success_all':"ตั้งแต้มเรียนรู้ใน %s โหมดของ %s เป็น %s สำหรับ %s แล้ว",
S+'mode_learning.success_everything':"ตั้งแต้มเรียนรู้ในทุกโหมดของอินสแตนซ์ %s เป็นค่าสูงสุดสำหรับ %s แล้ว",
S+'predator.block_mode.all':"เปลี่ยนการกลืนบล็อกของ %s เป็นทั้งหมด",
S+'predator.block_mode.blocks':"เปลี่ยนการกลืนบล็อกของ %s เป็นบล็อก",
S+'predator.block_mode.fluid':"เปลี่ยนการกลืนบล็อกของ %s เป็นของเหลว",
S+'predator.block_mode.none':"เปลี่ยนการกลืนบล็อกของ %s เป็นไม่มี",
S+'preset.changed':"เปลี่ยนพรีเซ็ตที่ใช้งานเป็น %s",
S+'preset.changed_name':"เปลี่ยนชื่อพรีเซ็ต %s เป็น %s",
S+'preset.changed_spell':"เปลี่ยนเวทที่ใช้งานเป็น %s",
S+'preset.no_change':"พรีเซ็ตที่ใช้งานของคุณเป็น %s อยู่แล้ว",
S+'reflector.remaining_echo':"แต้ม Echo: %s",
S+'set_cooldown.all':"ตั้งคูลดาวน์ของ %s สำหรับทุกอินสแตนซ์ %s เป็น %s วินาทีแล้ว",
S+'set_cooldown.all.no_changes':"ไม่มีความสามารถของ %s ที่ได้รับผลกระทบ",
S+'set_cooldown.no_changes':"คูลดาวน์ของ %s ไม่ได้รับผลกระทบ",
S+'set_remove_time.all':"ตั้งเวลาลบของทุกอินสแตนซ์ของ %s เป็น %s วินาทีแล้ว",
S+'set_remove_time.no_changes':"เวลาลบของ %s ไม่ได้รับผลกระทบ",
S+'skill_list.empty':"%s ไม่มีความสามารถที่ตรงตามเงื่อนไข",
S+'skill_set.failed':"%s ตั้งในช่องไม่ได้",
S+'spatial_storage.failed':"%s ไม่ใช่ความสามารถ Spatial Storage",
S+'spatial_storage.full':"Spatial Storage ของ %s เต็ม",
S+'teleport.out_border':"คุณออกนอกขอบเขตโลกไม่ได้",
S+'teleport.warp_point.success':"วาร์ปไปยัง %s สำเร็จ",
S+'teleport.warp_point.wrong_dimension':"มิตินี้ไม่ตรงกับการตั้งค่าของจุดวาร์ปนี้",
S+'temporary.already_have':"คุณมี %s อยู่แล้ว",
S+'temporary.remove':"ลบ %s ชั่วคราวแล้ว",
S+'time_held.max':"เวลาเปิดใช้: %s/%s",
S+'toggle_all.off':"ปิดสกิล %s สำหรับ %s แล้ว",
S+'toggle_all.on':"เปิดสกิล %s สำหรับ %s แล้ว",
S+'toggle_off.already':"%s ถูกปิดอยู่แล้วสำหรับ %s",
S+'toggle_on.already':"%s ถูกเปิดอยู่แล้วสำหรับ %s",
S+'type.common':"ทั่วไป",
S+'type.extra':"Extra",
S+'type.intrinsic':"โดยกำเนิด",
S+'type.ultimate':"Ultimate",
S+'type.unique':"Unique",
}
def fb(a,v):
    if a.startswith('tensura.skill.mode.'): return v
run(116,D,fb)
