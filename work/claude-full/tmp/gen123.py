import sys
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp')
from gt import run
TB='tensura_tno.compat.tensurabarriers.'
G=TB+'guide.'
D={
G+'text.high_magisteel':"High Magisteel",
G+'text.pure_magisteel':"Pure Magisteel",
G+'text.adamantite':"Adamantite",
G+'text.hi_hi_irokane':"Hi'hi'irokane",
G+'anchor_size':"ขนาดอยู่ระหว่าง §6%1$s§r ถึง §6%2$s§r บล็อก บาเรียร์ที่ใหญ่กว่าเผาเชื้อเพลิงต่อวินาทีมากกว่า",
G+'anchor_tier':"§b%1$s§r: สูงสุด §6%2$s§r บล็อก, HP §6%3$sx§r, เชื้อเพลิง §6%4$sx§r, %5$s",
G+'core_slot':"%1$s ช่อง core",
G+'core_slots':"%1$s ช่อง core",
G+'starting_points':"คุณเริ่มต้นด้วย §6%1$s§r แต้ม",
G+'point_page':"สกิลให้แต้ม (%1$s)",
G+'mastery_page':"แต้มความชำนาญ (%1$s)",
G+'cooldown_bonus':"คูลดาวน์ preset §6x%1$s§r",
G+'health_bonus':"HP §6%1$s§r",
G+'cost_bonus':"ต้นทุน §6%1$s§r",
G+'integrity':"§bIntegrity§r เป็น modifier แบบมีระดับ (1-%1$s): แต่ละระดับเพิ่ม HP §6%2$s§r",
G+'acquisition':"§6Barrier Arts§r เรียนรู้ได้โดยชำนาญ §gMultilayer Barrier§r และ §gRanged Barrier§r%1$s",
G+'acquisition_alternative':" หรือโดยชำนาญเวทบาเรียร์ §6%1$s§r ใดๆ",
G+'skill_tag':" (§5%1$s§r)",
TB+'skill.barrier_arts.description':"ออกแบบบาเรียร์ของคุณเอง ใช้แต้มที่ได้จากสกิลของคุณกับ modifier ย่อตัว + Barrier Creation ซ่อมบาเรียร์ ย่อตัว + preset แสดงค่าสถานะของมัน",
'tensurabarriers.skill.barrier_arts.description':"ออกแบบบาเรียร์ของคุณเอง ใช้แต้มที่ได้จากสกิลของคุณกับ modifier ย่อตัว + Barrier Creation ซ่อมบาเรียร์ ย่อตัว + preset แสดงค่าสถานะของมัน",
'tensurabarriers.skill.admin_barrier.description':"Barrier Arts สำหรับผู้ดูแล",
'tensurabarriers.skill.barrier_master.description':"ความชำนาญเหนือบาเรียร์ ทุกบาเรียร์ที่คุณสร้างแข็งแกร่งและมีประสิทธิภาพขึ้น บาเรียร์พ้นคูลดาวน์เร็วขึ้นสองเท่าและได้ modifier บางอย่างโดยไม่ต้องมีสกิล",
'tensurabarriers.skill.barrier_master.containment.description':"กดเพื่อขว้างวงแหวนสามวงใส่ผู้ที่คุณมองอยู่ เมื่อโดนเป้าหมาย จะผนึกสกิล เวท และ battlewill ของมัน",
'tensurabarriers.skill.spatial_bind.description':"พันธนาการเป้าหมาย ห้ามไม่ให้ใช้สกิลมิติและเคลื่อนที่",
'tensurabarriers.skill.barrier_dispel.description':"ด้วยความชำนาญเวทบาเรียร์ระดับหนึ่ง เรียนรู้การสลายบาเรียร์โดยสมบูรณ์",
'tensurabarriers.skill.invasion.description':"ใช้เวทมิติระดับสูงบุกรุกบาเรียร์หากแข็งแกร่งพอ",
'tensurabarriers.skill.simple_barrier.description':"สร้างบาเรียร์ง่ายๆ รอบตัวคุณ คุณยังย่อตัวและมองเพื่อนเพื่อป้องกันเขาแทนได้",
'tensurabarriers.skill.defensive_wall.description':"ร่ายกำแพงป้องกันตรงหน้าคุณ",
'tensurabarriers.skill.black_casing.description':"สร้างบาเรียร์ที่ทำลายไม่ได้ แต่ทำให้คุณขยับไม่ได้และดูดมาจิคูล 5% ต่อวินาที",
'tensurabarriers.skill.barrier_formation.description':"สร้างบาเรียร์สำหรับตัวคุณเองหรือคุณและพันธมิตร HP ของบาเรียร์ถูกแบ่งระหว่างเป้าหมาย",
'tensura.attribute.barrier_boost':"Barrier Boost",
'tensura.attribute.barrier_cost':"Barrier Cost",
TB+'ui.name_hint':"ชื่อ",
TB+'ui.info':"ข้อมูล",
TB+'ui.name.block_entry':"Block Entry",
}
def fb(a,v):
    if a.startswith(G+'skill.'): return v
run(123,D,fb)
