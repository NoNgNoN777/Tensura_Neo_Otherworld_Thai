import sys
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp')
from gt import run
A='tensura.attribute.'
D={
'tensura.alignment.default':"ค่าเริ่มต้น",
'tensura.alignment.holy':"Holy",
'tensura.alignment.majin':"Majin",
'tensura.anvil.menu.open':"เปิดทั่ง",
'tensura.argument.race.invalid':"เผ่าที่ป้อนไม่ถูกต้อง",
'tensura.argument.skill.invalid':"อินสแตนซ์ที่ป้อนไม่ถูกต้อง",
A+'analysis_distance':"ระยะวิเคราะห์",
A+'analysis_level':"ระดับการวิเคราะห์",
A+'aura.name':"Aura",
A+'aura.shortened_name':"AP",
A+'aura_gain':"เปอร์เซ็นต์การได้ Aura",
A+'aura_regeneration_multiplier':"ตัวคูณการฟื้นฟู Aura",
A+'block.age':"อายุ",
A+'block.correct_tool':"เครื่องมือที่ถูกต้อง",
A+'block.egg_hatch':"การฟักไข่",
A+'block.explosion_resistance':"ความต้านทานการระเบิด",
A+'block.failed_growth':"การเติบโตล้มเหลว",
A+'block.hardness':"ความแข็ง",
A+'block.light_level':"ระดับแสง",
A+'chant_speed':"ความเร็วร่ายเวท",
A+'dark_vision':"การมองเห็นในที่มืด",
A+'darkness_boost':"Darkness Attack Boost",
A+'darkness_resist_degradation':"Darkness Resist Degradation",
A+'darkness_resistance':"Darkness Attack Resistance",
A+'dodge_invulnerability':"อมตะระหว่างหลบ",
A+'dodge_negate_chance':"โอกาสลบล้างการหลบ",
A+'dodge_strength':"พลังการหลบ",
A+'earth_boost':"Earth Attack Boost",
A+'earth_resist_degradation':"Earth Resist Degradation",
A+'earth_resistance':"Earth Attack Resistance",
A+'existence_points':"Existence Points",
}
def fb(a,v):
    if a.startswith('tensura.advancements.'): return v
run(110,D,fb)
