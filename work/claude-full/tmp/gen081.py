import json,sys
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=81
D={
'greatsage.whatsnew.0_0_7.4.title':"ทะเลวิญญาณ",
'greatsage.whatsnew.0_0_7.4.desc':"ฉากการเกิดใหม่ฉากใหม่: วาดความปรารถนาของคุณเหนือทะเลสาบวิญญาณใต้หมู่ดาว",
'greatsage.whatsnew.0_0_7.5.title':"การหลอมรวมสกิล",
'greatsage.whatsnew.0_0_7.5.desc':"เมื่อสกิลหลอมรวมเป็น Unique หรือ Ultimate สกิลจะพุ่งเข้าหน้าจอในรูปแบบการ์ดสกิลสไตล์อนิเมะ หน้าจอแตกเป็นเสี่ยง และเศษชิ้นส่วนประกอบกลับมาเป็นสกิลใหม่",
'greatsage.whatsnew.0_0_7.6.title':"การตั้งชื่อในรูปแบบคัตซีน",
'greatsage.whatsnew.0_0_7.6.desc':"ตั้งชื่อมอนสเตอร์แล้วกล้องจะเลื่อนไปด้านข้าง: มาจิคูลของคุณไหลเข้าสู่มันและมันเรืองแสงขณะดูดซับ จากนั้น Sage รายงานชื่อ และ Voice of the World ยืนยันวิวัฒนาการของมัน ผู้เล่นที่ถูกตั้งชื่อจะเห็นจากมุมของตนเอง ปิดได้ด้วย namingScene ใน client config",
'greatsage.whatsnew.0_0_7.7.title':"Thought Acceleration (H)",
'greatsage.whatsnew.0_0_7.7.desc':"เมื่อมี Great Sage หรือ Thought Acceleration กด H หรือพูดออกมา: โลกจะหยุดนิ่งในสีเย็น เสียงลากต่ำลง หัวใจของคุณเต้นแทนที่ทุกเสียง และโพรเจกไทล์ที่พุ่งเข้ามาจะแสดงเส้นทาง เป็นสีแดงหากจะโดนคุณ เล่นคนเดียว: โลกทั้งใบช้าลง x5 ผู้เล่นหลายคน: ฟองขนาด 20 บล็อกทำให้สิ่งมีชีวิตและโพรเจกไทล์ช้าลง 6 วินาที คูลดาวน์ 40 วินาที ปรับแต่งได้ทั้งคู่",
'greatsage.whatsnew.0_0_7.8.title':"Magic Sense (N)",
'greatsage.whatsnew.0_0_7.8.desc':"เมื่อมีสกิลรับรู้เช่น Magic Sense คุณจะเห็นออร่าของทุกสิ่งมีชีวิต ที่มีรูปร่างตามลำตัวของมัน สีของออร่าตามฝ่ายของมัน (ม่วง Majin, ขาวทอง Hero, แดง Chaos, เขียวกลาง) ขนาดตาม EP ของมันและโตขึ้นเรื่อยๆ ออร่าขนาดมหึมาในที่ไกลหมายความว่าให้วิ่งหนี ปรับแต่งได้ใน Settings",
'greatsage.whatsnew.0_0_7.9.title':"เติบโตเร็วขึ้น",
'greatsage.whatsnew.0_0_7.9.desc':"ได้ประสบการณ์เพิ่ม x1.5 การสังหารสปีชีส์ใดครั้งแรกนับเป็นการสังเกตมัน และไอเทมที่ถือเป็นครั้งแรกจะถูกประเมิน",
'greatsage.whatsnew.0_0_7.10.title':"การวิเคราะห์เป็นระยะและโหมดสกิล",
'greatsage.whatsnew.0_0_7.10.desc':"เมื่อใช้ร่วมกับ TNO การวิเคราะห์ให้ความชำนาญเป็นระยะ และไม่เติมแต้มเรียนรู้โหมดอีกต่อไป FoxAblaze Ultimate Raphael นับเป็น Great Sage ด้วย",
'greatsage.whatsnew.0_0_7.11.title':"Gamerule ที่ชัดเจนขึ้น",
'greatsage.whatsnew.0_0_7.11.desc':"needGreatSage กลายเป็น announcementsRequireGreatSage: ตัดสินเพียงว่าใครได้รับการประกาศ ใหม่: requireGreatSage (เปิดเป็นค่าเริ่มต้น) ปิดแล้วทุกคนใช้เมนู G การประเมิน คำสั่งเสียง และการวิเคราะห์ได้โดยไม่ต้องมีสกิล Great Sage",
'greatsage.whatsnew.0_0_7.12.title':"เมนูที่ชัดเจนขึ้น",
'greatsage.whatsnew.0_0_7.12.desc':"ปุ่มใหญ่ขึ้น ฟองของ Sage ไม่บังหน้าอีกต่อไป และระดับที่ถูกผนึกจะบอกให้เปิดในแผนผังการเติบโต",
'greatsage.whatsnew.0_0_7.13.title':"การแก้ไข",
'greatsage.whatsnew.0_0_7.13.desc':"การเกิดใหม่ไม่แจก Unique พิเศษจากแอดออนอีกต่อไป และความต้านทานจากแอดออนไม่เป็น Nuclear หรือ Void เสมอไปอีก ฟองการประเมินไม่ลอยหลุดเมื่อบิน ออร่าไม่ติดเป็นทรงแคปซูลกับบางม็อด และอาการค้างก่อนแอนิเมชันหายไป ผู้ดูแลเซิร์ฟเวอร์มี /greatsage xp คำสั่งเสียงใช้ได้กับไมโครโฟนที่ไม่รับ 16 kHz และเสียงหึ่งพื้นหลังของเมนูเบาลงมาก โมเดลเสียงภาษาโปรตุเกสและตุรกีติดตั้งได้ถูกต้อง ข้อความเมนูไม่ทะลุหน้าต่างยืนยัน การรีเซ็ตเต็มตอนนี้มอบ Unique ทุกตัวที่ Tensura ติดค้างคุณจากตัวนับการรีเซ็ต และคุณไม่อมตะต่อเนื่องหลังผลลัพธ์การเกิดใหม่ที่หายากอีกต่อไป",
'greatsage.thought.title':"Thought Acceleration",
'greatsage.thought.unable':"Thought Acceleration ต้องมี Great Sage (หรือ Thought Acceleration ของ Tensura)",
'greatsage.thought.cooldown':"Thought Acceleration กำลังชาร์จ: %s วินาที",
'greatsage.naming.title':"การตั้งชื่อ",
'greatsage.naming.evolved_form':"%s ที่วิวัฒนาการแล้ว",
'block.iceandfire.graveyard_soil.desc':"เสกผีในตอนกลางคืน",
'iceandfire.ponder.dragon_forge.header':"ใช้มังกรเพื่อขับเคลื่อน Dragon Forge",
'iceandfire.ponder.dragon_forge.text_1':"นี่คือแกนกลางของเตาหลอม ไอเทมทั้งหมดใส่ลงที่นี่",
'iceandfire.ponder.dragon_forge.text_2':"มังกรต้องมองเห็นบล็อกนี้เพื่อขับเคลื่อนเตาหลอม",
'iceandfire.ponder.dragon_forge.text_3':"คุณต้องใช้มังกรชนิดที่ถูกต้องเพื่อขับเคลื่อนเตาหลอม",
'iceandfire.ponder.dragon_forge.text_4':"คุณเปิดเตาหลอมได้โดยคลิกบล็อกที่กึ่งกลางของแต่ละด้าน",
'iceandfire.ponder.tag.dragon_forge':"Dragon Forge",
'iceandfire.ponder.tag.dragon_forge.description':"เตาหลอมสำหรับทำ dragon steel",
'item.dragonscales_armor.desc':"เพิ่มการป้องกันจากการโจมตีด้วยลมหายใจของมังกร",
'item.iceandfire.air_pods.desc':"โอ้พระเจ้า สตีฟใส่ AirPods อยู่ เขาไม่ได้ยินเราหรอก!",
'item.iceandfire.amphithere_arrow.desc':"ผลักมอนสเตอร์ทุกตัวถอยด้วยพลังจากปีกของ amphithere!",
'item.iceandfire.amphithere_macuahuitl.desc_0':"ผลักเอนทิตีขึ้นและถอยหลัง",
'item.iceandfire.amphithere_macuahuitl.desc_1':"ปิดการใช้งานโล่",
'item.iceandfire.amphithere_skull.jei_desc':"วางบนพื้นหรือผนังเป็นถ้วยรางวัลได้",
}
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    if a in D: out[k]=D[a]
    elif a.startswith('item.iceandfire.banner_pattern_'): out[k]=json.loads(v)
print('keys',len(keys),'out',len(out),[k.split('wiki.')[-1] for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
