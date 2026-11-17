import json,sys
sys.stdout.reconfigure(encoding='utf-8')
P='foxablazeaqzl_wiki.wiki.'
T={}
def ele(k,low,lowpct,high,hi):
    T[P+f'item.tensura.{k}_elemental_shard.description']=f"การได้รับ:\nไอเทมนี้ได้จากการสังหาร:\n- {low} โอกาส 25% ได้ 1 ชิ้น\n- {high} โอกาส 100% ได้ 1 - 3 ชิ้น\n===คำเตือน: Elemental ที่ถูกอัญเชิญไม่ดรอปเศษใดๆ===\n\nการใช้งาน:\nใช้คราฟต์ได้"
ele('earth','Beast Gnome',25,'War Gnome',0)
ele('fire','Salamander',25,'Ifrit',0)
ele('space','Winged Cat',25,'Akash',0)
ele('water','Aqua Frog',25,'Undine',0)
ele('wind','Feathered Serpent',25,'Sylphide',0)
for k,n in [('low_magisteel','Low Magisteel'),('high_magisteel','High Magisteel'),('mithril','Mithril'),('pure_magisteel','Pure Magisteel'),('orichalcum','Orichalcum'),('adamantite','Adamantite'),('hihiirokane',"Hihi'Irokane")]:
    T[P+f'item.tensura.{k}_bone_golem.description']=f"การได้รับ:\nคราฟต์ที่ Smithing Bench ด้วยวัสดุ {n}\n\nการใช้งาน:\nใช้เป็นไอเทม {n} Bone Golem"
T[P+'item.tensura.marionette_heart.description']="การได้รับ:\n- พบใน Ancient City (โอกาส 0.5%)\n- สมบัติ Bastion และ End City (ทั้งคู่โอกาส 1%)"
T[P+'item.tensura.battlewill_manual.description']="การได้รับ:\nพบใน:\n- Abandoned Mineshaft\n- Bastion (คอก Hoglin)\n- Desert Pyramid\n- Igloo\n- Ruined Portal\n- Spawner\n- Stronghold\n- Underwater ruin (ใหญ่)\n- Woodland Mansion\n- Trial Chambers Vault (ลูทปกติ)\n- Trial chambers Ominous Vault (ปกติ/Common)\nทุกสถานที่เหล่านี้มีโอกาส 50%\n\nการใช้งาน:\nให้สกิล battlewill หนึ่งอย่างจากหลายอย่างแบบสุ่ม หนังสืออาจพยายามให้สกิลที่คุณรู้อยู่แล้ว ส่งผลให้ไม่ได้เรียนรู้สกิลใดและแสดงข้อความ \"You already had (Battlewill Skill)\""
T[P+'item.tensura.monster_saddle.description']="ขณะนี้หน้า wiki ไม่มีข้อความรายละเอียดเกี่ยวกับการได้รับหรือการใช้งาน"
T[P+'item.tensura.slime_in_a_bucket.description']="การได้รับ:\nไอเทมนี้ได้จากการคลิกขวาที่ Slime ด้วย Bucket\n\nการใช้งาน:\n???"
T[P+'item.tensura.labyrinth_explorer_map.description']="การได้รับ:\nDwarf Cartographer ระดับ Master เสนอแลกเปลี่ยนให้ได้\n\nการใช้งาน:\nใช้ค้นหา Labyrinth Tree คล้ายแผนที่นักสำรวจของ vanilla"
T[P+'item.tensura.hell_gate_explorer_map.description']="การได้รับ:\nDwarf Cartographer ระดับ Master เสนอแลกเปลี่ยนให้ได้\n\nการใช้งาน:\nใช้ค้นหา Hell Gate คล้ายแผนที่นักสำรวจของ vanilla"
T[P+'item.tensura.race_reset_scroll.description']="การได้รับ:\nได้จากการคราฟต์เท่านั้น\n===การคราฟต์===\nสูตรคราฟต์\n\nการใช้งาน:\n- รีเซ็ตสเตตัส ชื่อ สถานะการตื่นรู้ วิญญาณ ความต้านทาน และเผ่าของผู้ใช้ พร้อมสกิล Intrinsic ของเผ่า\n- คูลดาวน์ 5 วินาที"
T[P+'item.tensura.skill_reset_scroll.description']="การได้รับ:\n===การคราฟต์===\nสูตรคราฟต์\n\nการใช้งาน:\n- รีเซ็ตสกิลทุกประเภททุกอย่างของผู้ใช้ ยกเว้นสกิล Intrinsic ของเผ่า\n- คูลดาวน์ 5 วินาที\nScroll นี้ไม่ครอบคลุมค่าใช้จ่ายของ Unique Skill ใหม่ โปรดระวัง ไม่เช่นนั้นคุณอาจไม่มี Unique Skill เลย\nต้องมี MP สูงสุด 100K เพื่อให้ unique skill ทั้งหมดสุ่มใหม่ได้ ต่ำกว่านั้นคุณอาจมีไม่พอสำหรับสกิลที่สุ่มได้และจะไม่ได้รับมัน\n''MP หมายถึงมาจิคูล''"
T[P+'item.tensura.character_reset_scroll.description']="การได้รับ:\n===การคราฟต์===\nสูตรคราฟต์\n===Smithing Bench===\nสูตร Smithing\n\nการใช้งาน:\nรีเซ็ตทุกอย่างของผู้ใช้ เกือบเหมือนเกิดใหม่ตั้งแต่ต้น\nรวมถึง achievement ที่คุณได้รับด้วย\nใช้กับกลไก gamerule Reset Counter ด้วย\n- คูลดาวน์ 5 วินาที"
dom="เชี่ยวชาญสกิล manipulation ที่เป็นเงื่อนไขและมี EP ตามเกณฑ์ domination ที่ตั้งค่าไว้"
for k in ['tensura.earth_domination','tensura.flame_domination','tensura.gravity_domination','tensura.lightning_domination','tensura.sound_domination','tensura.spatial_domination','tensura.water_domination','tensura.weather_domination','tensura.wind_domination','mysticism.darkness_domination','mysticism.ice_domination','mysticism.light_domination']:
    T[P+f'evolution.{k}.description']=dom
T[P+'evolution.tensura.gluttony.description']="เงื่อนไขรวม: มี Starved และชำนาญ Predator กฎการได้รับและการจ่ายของ Gluttony ก็มีผลด้วย"
d2="เงื่อนไขการได้รับเริ่มต้น: ชำนาญสกิลนี้และมีความจุมาจิคูลตามเป้าหมาย เซิร์ฟเวอร์เปลี่ยนเงื่อนไขและการตั้งค่าความชำนาญได้"
for k in ['witch_of_vainglory','schwi_ex_machina','mammon_casino','divine_general_mahoraga','kronairos_lord_of_the_endless','axiom_lord_of_reflected_judgment','morph','elfaria_the_hallowed_icemaiden','abhoth_lord_of_pestilence','witch_of_envy_satella']:
    T[P+f'evolution.tensuramoreskills.{k}.description']=d2
T[P+'evolution.tensuramoreskills.true_authority_of_greed.description']="โดยค่าเริ่มต้น ชำนาญ Authority of Greed และมีความจุมาจิคูลตามที่ตั้งค่าไว้ การเรียนรู้ True Authority จะลบ Authority of Greed เดิม เงื่อนไขปรับได้"
T[P+'evolution.tensuramoreskills.michael_angel_of_locks.description']="ต้องมีทั้ง Infinity Prison และ Suppressor โดยค่าเริ่มต้น Infinity Prison ต้องชำนาญและตรงตามเงื่อนไขมาจิคูลที่ตั้งค่าไว้ การได้รับถาวรจะใช้สกิลทั้งสอง"
T[P+'evolution.tensuramoreskills.pain_lord_of_six_paths.description']="เงื่อนไขรวมเริ่มต้น: ชำนาญ Oppressor และมี Gravity Manipulation เกณฑ์ EP และความจุมาจิคูลที่ตั้งค่าไว้ก็มีผลด้วย"
T[P+'evolution.foxablazeultimate.raphael.description']="หลอมรวม Great Sage และ Degenerate ที่ชำนาญแล้ว โดยใช้ทั้งสอง หากเปิดใช้ ต้องมีสถานะ Hero Egg, True Hero, Demon Lord Seed หรือ True Demon Lord กฎความไม่ซ้ำก็มีผล"
T[P+'evolution.foxablazeultimate.beelzebuth.description']="หลอมรวม Gluttony และ Merciless ที่ชำนาญแล้ว เงื่อนไขสถานะที่ตั้งค่าไว้และกฎความไม่ซ้ำก็มีผลด้วย"
T[P+'evolution.foxablazeultimate.ciel.description']="Raphael ถาวรถูกแทนที่ด้วย Ciel เมื่อตื่นรู้ ความชำนาญ สถานะ True Demon Lord หรือ True Hero แกน Charybdis ที่รวมแล้ว จำนวนไอเทมที่กลั่น และตัวกระตุ้นการต่อสู้เมื่อพลังชีวิตต่ำที่ตั้งค่าไว้มีผลทั้งหมด"
T[P+'evolution.foxablazeultimate.uriel.description']="ใช้การสังเคราะห์ของ Raphael เพื่อวิวัฒนาการ Infinity Prison ที่ชำนาญแล้วเป็น Uriel โดยใช้ Infinity Prison กฎความไม่ซ้ำมีผล"
T[P+'evolution.foxablazeultimate.shub_niggurath.description']="ต้องมี (Raphael หรือ Ciel) ที่ชำนาญถาวร และ Uriel และ Beelzebuth สถานะ True Demon Lord จำนวนสกิลที่ชำนาญตามที่ตั้งค่า EP สูงสุด และมาจิคูลปัจจุบัน เงื่อนไขก่อนหน้ายังคงอยู่ มาจิคูลที่ตั้งค่าไว้จะถูกใช้"
T[P+'evolution.foxablazeultimate.yog_sothoth.description']="ต้องมี Infinity Prison, Absolute Severance, Usurper และ Time Traveler ที่ชำนาญถาวร การสังเคราะห์ของ Raphael ยังต้องมีสกิลความเข้ากันได้ทางเลือก มาจิคูลสูงสุดพื้นฐานเพียงพอ และสิทธิ์ความไม่ซ้ำ"
T[P+'evolution.foxablazeultimate.velgrynd.recipe.foxablazeultimate.velgrynd_acquisition.description']="เงื่อนไขร่วมเริ่มต้น: เป็นเจ้าของและชำนาญ Flame Domination, Flame Breath, Thought Acceleration และ Spatial Manipulation ถาวรเพื่อวิวัฒนาการอัตโนมัติ โดยค่าเริ่มต้น จะใช้มาจิคูลสูงสุดพื้นฐาน 3,000,000 อย่างถาวร โบนัสความจุชั่วคราวไม่นับ เฉพาะ Flame Breath ที่ถูกใช้เมื่อสำเร็จ อีกสามอย่างคงความชำนาญไว้ การตั้งค่าการได้รับอัตโนมัติ เงื่อนไขที่ตั้งค่า การตั้งค่าความชำนาญและการใช้ และกฎความไม่ซ้ำทั้งเซิร์ฟเวอร์มีผล"
d3="การชำนาญสกิลที่เป็นเงื่อนไขเองจะปลดล็อกอินสแตนซ์การเรียนรู้เป้าหมาย สกิลที่เป็นเงื่อนไขยังคงอยู่"
for k in ['thought_communication','multilayer_barrier','hydraulic_propulsion','heat_wave','mortal_fear','spatial_manipulation']:
    T[P+f'evolution.tensura.{k}.description']=d3
d4="ชำนาญสกิลที่เป็นเงื่อนไขและมี EP ตามเกณฑ์การได้รับที่ตั้งค่าไว้ของเป้าหมาย"
for k in ['voice_cannon','haki','water_blade']:
    T[P+f'evolution.tensura.{k}.description']=d4
T[P+'evolution.tensura.magic_sense.description']="การได้รับ Danger Sense ถาวรจะปลดล็อกอินสแตนซ์การเรียนรู้ Magic Sense เพิ่มด้วย Danger Sense ยังคงอยู่"
T[P+'evolution.tensura.sense_soundwave.description']="ต้องชำนาญ Danger Sense และ Magic Sense การได้รับหรือ callback ความชำนาญที่ตรงกันจะปลดล็อกอินสแตนซ์การเรียนรู้ Sense Soundwave"
T[P+'evolution.tensura.universal_perception.description']="ต้องชำนาญ Magic Sense และได้ Sense Heat Source และ Sense Soundwave ถาวร ปลดล็อกอินสแตนซ์การเรียนรู้ Universal Perception"
T[P+'evolution.tensura.ultraspeed_regeneration.description']="ชำนาญ Self Regeneration, เอาชนะ Charybdis อย่างน้อยหนึ่งครั้ง และมี EP ตามเกณฑ์การได้รับที่ตั้งค่าไว้"
T[P+'evolution.tensura.infinite_regeneration.description']="มี Ultraspeed Regeneration และมี EP ตามเกณฑ์ Infinite Regeneration ไม่ต้องชำนาญ Ultraspeed Regeneration ในที่นี้"
T[P+'evolution.tensura.hero_haki.description']="มี Haki, มี alignment ที่ไม่ใช่ Majin และมี EP ตามเกณฑ์การได้รับ Hero Haki"
T[P+'evolution.tensura.demon_lord_haki.description']="มี Haki, มี alignment ที่กลายเป็น Demon Lord ได้ และมี EP ตามเกณฑ์การได้รับ Demon Lord Haki"
T[P+'evolution.tensura.sacred_haki.description']="ชำนาญ Hero Haki และบรรลุสถานะ True Hero"
T[P+'evolution.tensura.law_manipulation.description']="การชำนาญ Analyst เองจะให้ Law Manipulation เพิ่มพร้อมคงไว้ซึ่ง Analyst การให้นี้เป็นไปตามระยะเวลาของอินสแตนซ์ต้นทาง"
T[P+'evolution.tensura.godly_craftsman.description']="ชำนาญ Researcher เพื่อได้ Godly Craftsman เอนแชนต์ที่เก็บไว้จะถูกโอนเมื่อสำเร็จ"
T[P+'evolution.tensura.gravity_manipulation.description']="การได้รับ Oppressor ถาวรจะปลดล็อกอินสแตนซ์การเรียนรู้ Gravity Manipulation เพิ่มด้วย Oppressor ยังคงอยู่"
d5="ชำนาญการแปลงร่างธาตุที่ตรงกันและมี EP ตามเกณฑ์การแปลงร่างธาตุเวทที่ตั้งค่าไว้"
for k in ['darkness','earth','flame','light']:
    T[P+f'evolution.tensura.magic_{k}_transform.description']=d5
json.dump(T,open(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp\t057.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(T))
T[P+'item.tensura.element_core_wind.description']="การได้รับ:\nมี 2 วิธีในการได้รับ:\n===\"จับ\" วิญญาณชั้นสูง===\nได้จากการคลิกขวาที่ Sylphide ด้วย Element Core (Empty)\n===การคราฟต์===\nสูตรคราฟต์\n\nการใช้งาน:\nใช้สำหรับใส่ช่อง\nเอฟเฟกต์: ให้การโจมตีพิเศษที่ยิงกระสุนลมตรงสร้างความเสียหาย 30 เพิ่มความเสียหายธาตุให้อาวุธ: +30 สำหรับแกนแรกและ +15 สำหรับแกนเพิ่มเติมแต่ละแกนที่ติดตั้ง"
json.dump(T,open(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp\t057.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
