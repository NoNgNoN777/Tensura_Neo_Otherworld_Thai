import sys
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp')
from gt import run
T='task.tensura_guild.'
def d(n,t): return (T+n+'.description',t)
ESS=lambda tail:tail
items=[
('screen.tensura_guild.info.completed_tasks',"สำเร็จแล้ว: "),
('screen.tensura_guild.info.active_tasks',"กำลังทำ: "),
('screen.tensura_guild.info.success_rate',"อัตราสำเร็จ: "),
('screen.tensura_guild.info.failure_record',"ล้มเหลว/ผิดสัญญา: "),
('screen.tensura_guild.info.current_race',"เผ่า: "),
('screen.tensura_guild.info.origin',"ถิ่นกำเนิด: "),
('screen.tensura_guild.info.dwarf_reputation',"ชื่อเสียงดวอร์ฟ: "),
d('kill_5_slimes',"ดูเหมือนหนองน้ำจะเป็นถิ่นอาศัยของสไลม์ สังหารสไลม์ 5 ตัว แล้วกลับมารายงาน"),
d('kill_4_8_tensura_slimes_f',"พบฝูงสไลม์ในป่า รับคอมมิชชันเพื่อรับเป้าหมาย 4 ถึง 8 ตัว แล้วกลับมาหลังปราบเสร็จ"),
d('kill_5_hound_dogs',"Hound Dog ที่ถูกขับเคลื่อนด้วยเวทเรียกคุกคามเส้นทางใกล้เคียง สังหาร Hound Dog 5 ตัว แล้วกลับมาส่งคอมมิชชัน"),
d('kill_5_barghests',"เสียงหอนของ Barghest ทำให้นิคมใกล้เคียงไม่สงบ และเปลวเพลิงสีดำของพวกมันอันตราย สังหาร Barghest 5 ตัว แล้วกลับมาส่งคอมมิชชัน"),
d('collect_5_magic_ore_shards',"เศษแร่เวทแตกออกจากเส้นแร่ที่อุดมด้วยมาจิคูล กิลด์ต้องการตัวอย่างสำหรับการประเมิน นำเศษแร่เวท 5 ชิ้นกลับมาส่ง"),
d('collect_10_medium_quality_magic_crystals',"คริสตัลเวทคุณภาพปานกลางเก็บมาจิคูลได้คงที่กว่า กิลด์กำลังเติมวัสดุวิจัย นำคริสตัล 10 ชิ้นกลับมาส่ง"),
d('collect_3_palm_saplings',"ต้นกล้าปาล์มมีประโยชน์ในการฟื้นฟูป่าชายฝั่งและขยายสวนที่กิลด์ดูแล นำต้นกล้าปาล์ม 3 ต้นกลับมาส่ง"),
d('collect_5_raw_blade_tiger_meat',"เนื้อ Blade Tiger เป็นเสบียงสนามที่มีค่าเมื่อปรุงสุก กิลด์ต้องการตัวอย่างสดสำหรับการจัดเสบียง นำเนื้อ Blade Tiger ดิบ 5 ชิ้นกลับมา"),
d('collect_5_raw_giant_bat_meat',"เนื้อ Giant Bat มักเก็บได้จากการล่าในถ้ำ นำเนื้อ Giant Bat ดิบ 5 ชิ้นกลับมาให้คลังกิลด์"),
d('craft_3_high_potions',"High Potion เป็นเสบียงฟื้นฟูที่เชื่อถือได้สำหรับคอมมิชชันอันตราย คราฟต์และส่ง High Potion 3 ขวด"),
d('collect_2_sissie_fins',"ครีบ Sissie ถือเป็นวัสดุปลาและมีประโยชน์ในการเตรียมอาหาร นำครีบ Sissie 2 ชิ้นกลับมา"),
d('collect_20_monster_leather_c',"หนังมอนสเตอร์ระดับ C ใช้ทำอุปกรณ์พื้นฐาน อานม้า และอุปกรณ์สนาม นำหนัง 20 ชิ้นกลับมา"),
d('collect_10_monster_leather_b',"หนังมอนสเตอร์ระดับ B แข็งแกร่งกว่าและเหมาะกับอุปกรณ์ที่ทนทานกว่า นำหนัง 10 ชิ้นกลับมา"),
d('collect_4_hipokute_flowers',"ดอก Hipokute เป็นวัสดุฟื้นฟูและส่วนผสมการกลั่นที่สำคัญ นำดอกไม้ 4 ดอกกลับมา"),
d('find_grimoire_d',"กิลด์กำลังเติมตำราเวทพื้นฐาน ค้นหา Grimoire (D) 1 เล่มจากซากหอคอยจอมเวทหรือคลังเวทเก่า แล้วนำกลับมา"),
d('find_grimoire_c',"Grimoire (C) เก็บบันทึกเวทที่คงที่กว่าสำหรับผู้เริ่มศึกษา ค้นหา Grimoire (C) 1 เล่มแล้วนำกลับมา"),
d('find_grimoire_b',"Grimoire ระดับ B หายากและมักถูกเก็บโดยนักวิจัยเวท ค้นหา Grimoire (B) 1 เล่มแล้วนำมาให้กิลด์ประเมิน"),
d('find_grimoire_a',"Grimoire (A) บันทึกระบบเวทระดับสูงกว่า กิลด์ต้องการตัวอย่างสำหรับหอจดหมายเหตุ ค้นหา 1 เล่มแล้วส่ง"),
d('find_grimoire_special_a',"ว่ากันว่า Grimoire (Special A) เป็นสมบัติของผู้ใช้เวทผู้ช่ำชองเท่านั้น หากพบ ให้นำกลับมาเก็บรักษา"),
d('collect_1_heavy_core',"Heavy Core เก็บพลังหนาแน่นผิดปกติและมีประโยชน์ต่อการประเมินระดับสูงของกิลด์ ได้รับ Heavy Core 1 ชิ้นแล้วส่ง"),
d('collect_1_marionette_heart',"Marionette Heart เป็นวัสดุเวทหายากที่มีคุณสมบัติเปลี่ยนชีวิตอันตราย ได้รับ Marionette Heart 1 ชิ้นแล้วส่ง"),
d('collect_1_darkness_core',"Darkness Core ปล่อยพลังมืดที่ไม่เสถียร กิลด์ต้องการตัวอย่างเพื่อยืนยันการใช้งาน ได้รับ Darkness Core 1 ชิ้นแล้วส่ง"),
d('kill_1_elemental_colossus',"Elemental Colossus มีแรงกดดันเกินกว่ามอนสเตอร์ธรรมดามาก เฉพาะนักผจญภัยที่เตรียมพร้อมเท่านั้นควรเข้าใกล้ สังหาร Elemental Colossus 1 ตัว แล้วกลับมาส่งคอมมิชชัน"),
d('kill_1_supermassive_slime',"กิลด์ตรวจพบ Supermassive Slime ที่พองตัวผิดปกติท่องไปใกล้ๆ เดินทางไปยังพิกัดที่ทำเครื่องหมาย ล่อมันออกมา และปราบก่อนที่มันจะคลั่ง"),
d('party_clear_giant_ant_nest',"คอมมิชชันหน่วย หน่วยต้องมีสมาชิกมากกว่า 1 คน กำจัด Giant Ant 20 ตัวภายใน 150 บล็อกจากรัง Giant Ant รางวัลเหรียญเงิน 30 เหรียญแบ่งในหน่วย และสมาชิกแต่ละคนได้ EXP ผจญภัย 25"),
d('clear_20_black_spiders_nest_c',"Black Spider ปิดกั้นเส้นทางใกล้รังของพวกมัน เดินทางไปยังรัง Black Spider กำจัด Black Spider 20 ตัวภายใน 150 บล็อกจากรัง แล้วกลับมาส่งคอมมิชชัน"),
d('investigate_wizard_tower_c',"กิลด์ต้องการรายงานเกี่ยวกับหอคอยจอมเวทร้าง เดินทางไปยังพิกัดที่ทำเครื่องหมาย ค้นหาและสืบสวนหอคอยจอมเวทใดๆ แล้วกลับมาส่งคอมมิชชัน"),
d('kill_3_giant_cod_f',"Giant Cod กำลังแย่งแหล่งประมงชายฝั่ง ปราบ Giant Cod 3 ตัว แล้วกลับกิลด์เพื่อส่งคอมมิชชัน"),
d('kill_3_giant_salmon_f',"ฝูง Giant Salmon กำลังทำลายอวนและขัดขวางทางน้ำ ปราบ Giant Salmon 3 ตัว แล้วกลับกิลด์เพื่อส่งคอมมิชชัน"),
d('collect_3_battlewill_manuals',"ตำรา Battlewill มักเก็บไว้ใกล้สนามฝึกยุทธ์ กิลด์ต้องการสักสองสามเล่มสำหรับหลักสูตรต่อสู้ระดับต้น เก็บตำรา Battlewill 3 เล่มแล้วส่ง"),
d('craft_20_training_dummies',"หุ่นฝึกสึกหรอเร็วในลานฝึก กิลด์ต้องการชุดใหม่สำหรับการฝึกพื้นฐาน คราฟต์หุ่นฝึก 20 ตัวแล้วส่ง"),
d('craft_8_bricks_magic_engines',"เครื่องยนต์เวทอิฐช่วยให้สิ่งอำนวยความสะดวกที่ขับเคลื่อนด้วยมาจิคูลมั่นคง คราฟต์เครื่องยนต์เวทอิฐ 8 เครื่องประเภทที่ตรงกันใดๆ แล้วส่ง"),
d('collect_64_oak_tool_racks',"คลังกิลด์กำลังจัดอุปกรณ์ฝึกใหม่และต้องการชั้นวางเครื่องมือจำนวนมากสำหรับอุปกรณ์ประจำวัน เก็บชั้นวางเครื่องมือ 64 ชิ้นประเภทที่ตรงกันใดๆ แล้วส่ง"),
d('craft_2_kiln_mithril',"เตาเผา Mithril ทนความร้อนที่จำเป็นต่อการแปรรูปวัสดุขั้นสูงและสำคัญต่อการขยายโรงงาน คราฟต์เตาเผา Mithril 2 เตาแล้วส่ง"),
]
ESSD="ร่องรอยแปลกประหลาด"
ess=[
('collect_2_cryptid_essences','Cryptid essence',"Cryptid essence มีร่องรอยประหลาดที่มีประโยชน์ในการติดตามสายพันธุ์มอนสเตอร์ที่ไม่รู้จัก เก็บ Cryptid essence 2 ชิ้นแล้วส่ง"),
('collect_2_flame_essences','Flame essence',"Flame essence เก็บมาจิคูลธาตุความร้อนเข้มข้นสำหรับทดสอบวัสดุทนความร้อน เก็บ Flame essence 2 ชิ้นแล้วส่ง"),
('collect_2_ice_essences','Ice essence',"Ice essence ปล่อยมาจิคูลธาตุเย็นสำหรับการเก็บรักษาตัวอย่างและวิจัยธาตุน้ำแข็ง เก็บ Ice essence 2 ชิ้นแล้วส่ง"),
('collect_2_lightning_essences','Lightning essence',"Lightning essence มีมาจิคูลที่มีประจุไม่เสถียรที่ใช้ทดสอบอุปกรณ์นำเวท เก็บ Lightning essence 2 ชิ้นแล้วส่ง"),
('collect_2_dragon_essences','Dragon essence',"Dragon essence คงแรงกดดันของมอนสเตอร์มังกรที่ทรงพลัง และมีค่าสำหรับบันทึกมอนสเตอร์ระดับสูง เก็บ Dragon essence 2 ชิ้นแล้วส่ง"),
('collect_2_elemental_essences','Elemental essence',"Elemental essence เก็บมาจิคูลธาตุวิญญาณไว้เปรียบเทียบปฏิกิริยาธาตุ เก็บ Elemental essence 2 ชิ้นแล้วส่ง"),
('collect_2_zane_blood','Zane blood',"Zane blood เป็นตัวอย่างวิจัยที่หายากและอันตรายซึ่งกิลด์ต้องผนึกไว้ เก็บ Zane blood 2 ชิ้นแล้วส่ง"),
('collect_4_blade_tiger_tails','Blade tiger tail',"หาง Blade Tiger คงเส้นใยมาจิคูลคมกริบที่มีประโยชน์ในงานอาวุธเบาและรายงานการติดตาม เก็บหาง Blade Tiger 4 ชิ้นแล้วส่ง"),
('collect_10_monster_leather_special_a','',"หนังมอนสเตอร์ Special A แข็งแกร่งเป็นพิเศษและมีค่าสำหรับเกราะขั้นสูงและถุงผนึก เก็บ 10 ชิ้นแล้วส่ง"),
('collect_15_monster_leather_a','',"หนังมอนสเตอร์ระดับ A เหมาะกับการเสริมอุปกรณ์สนาม และสำนักงานเสบียงของกิลด์ต้องการสต็อกที่สม่ำเสมอ เก็บ 15 ชิ้นแล้วส่ง"),
('collect_10_high_quality_magic_crystals','',"คริสตัลเวทคุณภาพสูงเก็บกระแสมาจิคูลหนาแน่นกว่า และจำเป็นสำหรับบำรุงรักษาสิ่งอำนวยความสะดวกขั้นสูงของกิลด์ เก็บ 10 ชิ้นแล้วส่ง"),
('collect_10_steel_threads','',"เส้นด้ายเหล็กบางและเหนียว มีประโยชน์ต่อกับดัก การเย็บ และการทดสอบควบคุมเส้นด้าย เก็บเส้นด้ายเหล็ก 10 เส้นแล้วส่ง"),
('collect_3_unicorn_horns','',"เขา Unicorn เก็บมาจิคูลบริสุทธิ์สำหรับการทดลองชำระล้างและงานอาวุธพิเศษ เก็บเขา Unicorn 3 ชิ้นแล้วส่ง"),
('collect_2_daemon_essences','',"Daemon essence มีคลื่นธาตุมืดแรงกล้าและช่วยให้จดหมายเหตุ daemon ของกิลด์สมบูรณ์ เก็บ Daemon essence 2 ชิ้นแล้วส่ง"),
('collect_1_slime_staffs','',"Staff of Slime ส่งอิทธิพลต่อสไลม์ใกล้เคียงได้ และกิลด์ต้องการหนึ่งอันสำหรับบันทึกการเลี้ยงเชื่อง ค้นหา staff of slime 1 อันแล้วส่ง"),
('collect_64_raw_silver','',"Raw silver เป็นวัสดุหลักสำหรับเหรียญและอุปกรณ์นำเวท เก็บ raw silver 64 ชิ้นแล้วส่ง"),
('collect_16_baffledils','',"Baffledil มีประโยชน์ในงานกลั่นที่เกี่ยวกับการสะกดจิตและการแพทย์สนาม เก็บ Baffledil 16 ต้นแล้วส่ง"),
('collect_1_nether_star','',"Nether star เป็นแกนหายากสำหรับงาน beacon ระดับสูงและทดสอบอุปกรณ์เวท ได้รับ nether star 1 ดวงแล้วส่ง"),
('collect_1_slime_king_summon','',"กิลด์กำลังรวบรวมตัวเร่งการเรียก Slime King เพื่อวิจัยภัยคุกคามบอส ได้รับ Slime King summon 1 ชิ้นแล้วส่ง"),
('craft_1_pouch_d','',"Coin Pouch (D) มีประโยชน์ในการจัดการการจ่ายเงินคอมมิชชันระดับเริ่มต้น คราฟต์ Coin Pouch (D) 1 ใบแล้วส่ง"),
('craft_1_pouch_c','',"Coin Pouch (C) จำเป็นสำหรับการจ่ายเงินสนามที่ใหญ่ขึ้นและการทำบัญชีเสบียง คราฟต์ Coin Pouch (C) 1 ใบแล้วส่ง"),
('craft_1_pouch_b','',"Coin Pouch (B) พกเงินรางวัลที่หนักขึ้นสำหรับคอมมิชชันขั้นสูงได้อย่างปลอดภัย คราฟต์ Coin Pouch (B) 1 ใบแล้วส่ง"),
('kill_3_army_wasps','',"Army Wasp คุกคามนักเดินทางจากอากาศและทำให้กองคาราวานกระจัดกระจายได้เร็ว สังหาร Army Wasp 3 ตัว แล้วกลับมาส่งคอมมิชชัน"),
('kill_5_giant_ants','',"Giant Ant ขุดเข้าไปในถนนและคลังเสบียงหากปล่อยไว้ สังหาร Giant Ant 5 ตัว แล้วกลับมาส่งคอมมิชชัน"),
('kill_8_hover_lizards','',"Hover Lizard กำลังรบกวนเส้นทางที่ลุ่มใกล้ดินแดนลิซาร์ดแมน สังหาร Hover Lizard 8 ตัว แล้วกลับมาส่งคอมมิชชัน"),
]
D={}
for a,b in items: D[a if not a.startswith('task.') else a]=b
D2={}
for a,b in items: D2[a]=b
import re
for base,_,txt in ess:
    for suf in ('','_d','_c','_e','_f'):
        D2[T+base+suf+'.description']=txt
fixed={
T+'collect_1_slime_staffs_d.description':"Staff of Slime ส่งอิทธิพลต่อสไลม์ใกล้เคียงได้ และกิลด์ต้องการหนึ่งอันสำหรับบันทึกการเลี้ยงเชื่อง ค้นหา staff of slime 1 อันแล้วส่ง",
T+'collect_3_golden_apples.description':"ห้องพยาบาลของกิลด์ต้องการ golden apple สำหรับการรักษาฉุกเฉินและเสบียงฟื้นฟู เก็บ golden apple 3 ลูกแล้วส่ง",
T+'collect_5_diamonds.description':"เพชรเป็นวัสดุที่มั่นคงทนทานสำหรับการประเมินพื้นฐานและซ่อมอุปกรณ์ เก็บเพชร 5 เม็ดแล้วส่ง",
T+'collect_25_emeralds.description':"มรกตมีประโยชน์ในการชำระการค้าระหว่างกิลด์กับซัพพลายเออร์หมู่บ้าน เก็บมรกต 25 เม็ดแล้วส่ง",
T+'collect_2_netherite_ingots.description':"แท่ง Netherite เป็นโลหะระดับสูงที่หายาก กิลด์ต้องการสต็อกเล็กน้อยสำหรับเสริมอุปกรณ์ เก็บแท่ง Netherite 2 แท่งแล้วส่ง",
T+'collect_1_heart_of_the_sea.description':"Heart of the sea มีค่าสำหรับการสำรวจมหาสมุทรและวิจัยอุปกรณ์หายใจใต้น้ำ ค้นหา heart of the sea 1 ชิ้นแล้วส่ง",
T+'collect_32_honeycombs.description':"รวงผึ้งจำเป็นสำหรับขี้ผึ้ง งานผนึก และการบำรุงรักษาคลังกิลด์ตามปกติ เก็บรวงผึ้ง 32 ชิ้นแล้วส่ง",
T+'kill_unicorn_group_flower_forest_c.description':"ฝูง Unicorn กำลังกินทุ่งดอกไม้และรบกวนผู้เลี้ยงผึ้งใกล้เคียง เดินทางไปยังพิกัดที่ทำเครื่องหมายและกำจัดพวกมัน",
}
D2.update(fixed)
run(118,D2)
