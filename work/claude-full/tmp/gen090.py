import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=90
SENSE="สามารถปรับเข้ากับมาจิคูลที่อยู่ใกล้ๆ และใช้มันรับรู้สภาพแวดล้อมได้"
D={
'effect.mowziesmobs.suns_blessing.description':"ให้คุณบัญชาพลังแห่งดวงอาทิตย์",
'effect.mowziesmobs.geomancy.description':"ให้คุณบัญชาพลังแห่งผืนดิน",
'effect.mowziesmobs.frozen.description':"ป้องกันการกระทำทั้งหมดในช่วงเวลาสั้นๆ ความเสียหายจากไฟจะลบเอฟเฟกต์ก่อนกำหนด",
'effect.mowziesmobs.sunblock.description':"เพิ่มการฟื้นฟูและความต้านทานความเสียหายเล็กน้อย",
'effect.mowziesmobs.poison_resist.description':"ป้องกันสถานะเอฟเฟกต์ Poison",
'effect.mowziesmobs.eclipsed.description':"ป้องกันสถานะเอฟเฟกต์อื่นทั้งหมดขณะที่ทำงานอยู่",
'effect.mowziesmobs.fragility.description':"เพิ่มความเสียหายที่ได้รับ",
'entity.mowziesmobs.sculptor.boss_info.timer.text':"เวลาที่เหลือ",
'enchantment.mysticism.boreal_frost.desc':"การสร้างความเสียหายให้ศัตรูด้วยอาวุธนี้ทำให้ Permafrost ที่เย็นเฉียบและกัดกร่อนทิ่มแทงเข้าไปถึงตัวตนของพวกมัน",
'enchantment.mysticism.holy_flames.desc':"การสร้างความเสียหายให้ศัตรูด้วยอาวุธนี้ทำให้พวกมันลุกเป็นเปลวไฟ Brimstone ที่สว่างและทรงพลัง",
'gamerule.mpSkillCost.description':"Unique Skill ใช้ Soul Energy เมื่อได้รับหรือไม่",
'mysticism.race.amped_guitar_wolf.description':"Guitar Wolf ที่วิวัฒนาการแล้วและมีความเชื่อมโยงลึกซึ้งกับเสียง สามารถรบกวนเวทของศัตรูที่อยู่ใกล้ มักเป็นมอนสเตอร์ที่น่าเกรงขามและได้รับการยกย่อง",
'mysticism.race.ant.description':"มดเป็นสัตว์ตัวเล็กไร้ความกลัวที่มีเปลือกนอกทนทานอย่างไร้เหตุผล เป็นที่รู้จักว่าบึกบึนและล้มยาก เตรียมรับการต่อสู้ที่ยืดเยื้อหากเจอเข้า!",
'mysticism.race.antumbra_spirit_wolf.description':"สิ่งมีชีวิตที่น่ากลัวอย่างแท้จริง นี่คือ Direwolf ที่ \"วิวัฒนาการอย่างถูกต้อง\" และกลายเป็น Spiritual Lifeform แทบไม่มีกำเนิดขึ้นมาแม้สักครั้งในหนึ่งพันปี และ Direwolf กับ Light Fang ทั่วไปทุกตัวโค้งคำนับต่อสิ่งมีชีวิตนี้",
'mysticism.race.arch_angel.description':"มี Angel เพียงไม่กี่ตนที่ไปถึงจุดนี้เพราะขาดอีโก้",
'mysticism.race.arch_doll.description':"ผลของ Arch Daemon ที่สิงร่าง magisteel",
'mysticism.race.arch_fallen.description':"Arch Angel ที่ถูกมาจิคูลทำให้เสื่อมทราม แล้วเลือกละทิ้งแสงสว่างเพื่อความมืด",
'mysticism.race.army_wasp.description':"แมงป่องที่วิวัฒนาการแล้ว มีความสามารถบิดเบือนแรงโน้มถ่วงเอง มันลอยไปอย่างไร้จุดหมายและต่อยสิ่งที่มันสนใจแบบสุ่ม มันไม่เคยถูกล่ามากเกินไปเพราะธรรมชาติของมัน การป้องกันของมันจึงอ่อนแอมาก",
'mysticism.race.army_wasp_insectar.description':"WIP",
'mysticism.race.army_wasp_savant.description':"WIP",
'mysticism.race.ascended.description':"ไม่เป็นไรหากเจ้าจำอดีตของตัวเองไม่ได้ นั่นคือสิ่งที่พวกเขาบอกตัวเอง การยอมรับความจริงข้อนี้และโอบกอดมัน นั่นคือเหตุผลที่พวกเขาก้าวขึ้นเหนือทุกอุปสรรคเป็น Spiritual Lifeform ทั้งที่เผชิญความท้าทาย",
'mysticism.race.attuned_wyrm.description':"เผ่าไวร์มที่ยังหาธาตุที่จะวิวัฒนาไปไม่พบ มันค้นหาหนทางวิวัฒนาการขณะท่องไปในโลก",
'mysticism.race.beetle.description':"ด้วงเป็นแมลงที่โจมตีหนัก ทุ่มทุกอย่างไปกับพลังของมัน แม้จะเป็นหนึ่งในเผ่าที่แข็งแกร่งกว่า แต่การป้องกันของมันกล่าวได้ว่าไม่น่าประทับใจ",
'mysticism.race.black_fang.description':"Direwolf ที่มีความเชื่อมโยงกับเวท "+SENSE,
'mysticism.race.blazing_scorch_wolf.description':"Scorch Wolf ที่วิวัฒนาการแล้วและมีความเชื่อมโยงลึกซึ้งกับความร้อนและพลังงานบริสุทธิ์ สร้างพายุเพลิงที่อันตรายถึงตายได้ มักเป็นมอนสเตอร์ที่น่าเกรงขามและได้รับการยกย่อง",
'mysticism.race.blue_centipede.description':"ตะขาบที่วิวัฒนาการแล้ว เน้นความสามารถในการว่ายน้ำ มันชอบล่าในมหาสมุทรกว้างใหญ่ โดยใช้ความสามารถในการทำให้เป้าหมายอัมพาต",
'mysticism.race.blue_centipede_insectar.description':"WIP",
'mysticism.race.blue_centipede_savant.description':"WIP",
'mysticism.race.blue_fang.description':"Direwolf ที่มีความเชื่อมโยงกับน้ำ "+SENSE,
'mysticism.race.brown_fang.description':"Direwolf ที่มีความเชื่อมโยงกับผืนดิน "+SENSE,
'mysticism.race.centipede.description':"ตะขาบเป็นแมลงที่เน้นความเร็วและหนีจากเกือบทุกการต่อสู้ได้ ขาจำนวนมากชดเชยการขาดพลัง",
'mysticism.race.chaos_doll.description':"ผลของ Arch Doll ที่กลับขั้ว alignment กลายเป็นฝ่าย Chaos",
'mysticism.race.chaos_metalloid.description':"ผลของ Chaos Doll ที่บรรลุ Divinity และตื่นรู้",
'mysticism.race.charged_perforator.description':"การกลายพันธุ์ที่หายากของหนอน sculk มันกลืนกินแก่นของสายฟ้าเองและได้ความสามารถเฉพาะ แต่ตัวนี้... ดูแปลกๆ",
'mysticism.race.cherub.description':"Angel บริสุทธิ์ที่ทรงพลังเป็นอันดับสองเท่าที่เป็นที่รู้จัก",
'mysticism.race.corrosion_soul_insect.description':"WIP",
'mysticism.race.daemon_doll.description':"ผลของ Arch Doll ที่ได้รับชื่อ",
'mysticism.race.darkness_fang.description':"Direwolf ที่มีความเชื่อมโยงกับความมืด มันกลมกลืนไปกับเงาและล่องหนได้ มืดดั่งราตรี",
'mysticism.race.devil_doll.description':"ผลของ Daemon Doll ที่บรรลุ Divinity และตื่นรู้",
'mysticism.race.direwolf.description':"Direwolf เป็นมอนสเตอร์ชนิดที่ชอบก่อความวุ่นวาย ตัวที่ฉลาดและเป็นมิตรกว่าให้ผู้อื่นขี่หลังได้ มีศักยภาพการเติบโตสูง",
'mysticism.race.dissonance_deity.description':"สิ่งที่เคยเป็นหนอน sculk ได้หายไปอย่างแท้จริง \"อสูรร่างทอดยาวจากขอบฟ้าหนึ่งถึงอีกขอบฟ้าหนึ่ง และเรอพายุที่เตือนทุกคนถึงคำสัญญาของวีรบุรุษ: ว่าแผ่นดินนี้ และทุกผู้ที่อาศัยอยู่ จะไม่ต้องทุกข์อีกต่อไป...\" มันบรรลุ Divinity มีร่างกายอมตะที่ไม่แก่",
'mysticism.race.divine_blue_centipede.description':"WIP",
'mysticism.race.divine_elemental.description':"แง่มุมแห่งความสมบูรณ์แบบที่แทนธาตุของมันได้อย่างสมบูรณ์แบบ สิ่งมีชีวิตนี้มีเวทวิญญาณระดับเทพเจ้า เทียบเท่า Ultimate Skill ระดับ King ที่ล้างทวีปได้หากร่าย",
'mysticism.race.divine_majin_elemental.description':"แง่มุมแห่งความสมบูรณ์แบบที่แทนธาตุของมันได้อย่างสมบูรณ์แบบ สิ่งมีชีวิตนี้มีเวทวิญญาณระดับเทพเจ้า เทียบเท่า Ultimate Skill ระดับ King ที่ล้างทวีปได้หากร่าย",
'mysticism.race.divine_excelsius.description':"จุดสูงสุดของผู้ที่สูญเสียอดีต พวกเขาพบความหมายในชีวิตใหม่ ผลักดันผ่านความกังวลและความผิดทั้งหมดเพื่อบรรลุ Divinity",
'mysticism.race.divine_inferius.description':"จุดสูงสุดของผู้ที่สูญเสียอดีต พวกเขาพบความหมายในความตาย เอาชนะทุกสิ่ง แม้แต่ผู้ที่ลืมโลกอย่างแท้จริง เพื่อบรรลุ Divinity",
'mysticism.race.divine_tengu.description':"ผลของ Tengu ที่บรรลุ Divinity",
'mysticism.race.divine_wolf.description':"Direwolf ที่บรรลุ Divinity มีร่างกายอมตะที่ไม่แก่",
'mysticism.race.dragonoid.description':"บุตรแห่งดวงดาวและความหวังของโลก คุณจะได้รับพลังที่แท้จริงไหม? คุณวิวัฒนาการได้เพียงครั้งเดียว แต่ค่าสถานะของคุณเติบโตตาม EP",
'mysticism.race.drone_beetle.description':"ด้วงที่วิวัฒนาการแล้ว เน้นความเร็ว แลกความเสียหายกับความเร็ว ตอนนี้บินได้ แต่ยังเด็กเกินไป",
'mysticism.race.drone_beetle_insectar.description':"Drone Beetle ที่ได้ร่างมนุษย์ ปีกแข็งแกร่งกว่ามากและเดินทางได้เร็วกว่ามาก",
'mysticism.race.drone_beetle_savant.description':"Drone Beetle ที่วิวัฒนาการ \"อย่างถูกต้อง\" และกลายเป็นสิ่งมีชีวิตวิญญาณ มันบินด้วยความเร็วมหาศาล แทบทะลุกำแพงเสียงด้วยความเร็วที่บิน",
'mysticism.race.earth_soul_insect.description':"Hardshell Ant ที่วิวัฒนาการ \"อย่างถูกต้อง\" และกลายเป็นสิ่งมีชีวิตวิญญาณ มันแทนธาตุดินได้อย่างสมบูรณ์แบบ ปกป้องผู้อ่อนแอและต่อสู้กับผู้ที่ทำผิดต่อมัน",
'mysticism.race.elemental_lord.description':"Elemental ที่วิวัฒนาการแล้วอย่างสง่างามและงดงาม ใช้เวทวิญญาณระดับ Lord ที่ทรงพลัง สามารถสู้ประชิดกับ Ultimate Skill ได้",
'mysticism.race.empty.description':"Remnant ที่เลือกทางออกที่ยากลำบาก แทนที่จะยอมรับอดีตที่ถูกลืม พวกเขาเลือกสู้กับมัน แต่ไร้ผล เปลือกที่ใหญ่กว่าและว่างเปล่ากว่ารออยู่",
'mysticism.race.enflamed_aberration.description':"สิ่งมีชีวิตเหล่านี้วิวัฒนาการให้ดูคล้ายคู่เทียบใน overworld อย่างน่าขนลุก ขอภาวนาว่าพลังของมันไม่ถูกปลดปล่อยอย่างแท้จริง มันเป็นสิ่งมีชีวิตกึ่งวิญญาณ",
'mysticism.race.fallen.description':"Seraph ที่ถูกมาจิคูลทำให้เสื่อมทราม แล้วเลือกละทิ้งแสงสว่างเพื่อความมืด",
'mysticism.race.fallen_arch_angel.description':"Arch Angel ที่ถูกมาจิคูลทำให้เสื่อมทราม แต่ก็ยังคงธาตุแสงไว้",
'mysticism.race.fallen_cherub.description':"Cherub ที่ถูกมาจิคูลทำให้เสื่อมทราม แต่ก็ยังคงธาตุแสงไว้",
'mysticism.race.fallen_greater_angel.description':"Greater Angel ที่ถูกมาจิคูลทำให้เสื่อมทราม แต่ก็ยังคงธาตุแสงไว้",
'mysticism.race.fallen_lesser_angel.description':"Lesser Angel ที่ถูกมาจิคูลทำให้เสื่อมทราม แต่ก็ยังคงธาตุแสงไว้",
'mysticism.race.fallen_lord.description':"Cherub ที่ถูกมาจิคูลทำให้เสื่อมทราม แล้วเลือกละทิ้งแสงสว่างเพื่อความมืด",
'mysticism.race.fallen_seraph.description':"Seraph ที่ถูกมาจิคูลทำให้เสื่อมทราม แต่ก็ยังคงธาตุแสงไว้",
'mysticism.race.fantasy_soul_insect.description':"Stag Beetle ที่วิวัฒนาการ \"อย่างถูกต้อง\" และกลายเป็นสิ่งมีชีวิตวิญญาณ มันแทนธาตุ Fantasy ได้อย่างสมบูรณ์แบบ บิดเบือนเวทและกำจัดภัยคุกคามด้วยพละกำลังล้วนๆ",
'mysticism.race.field_officer.description':"วิวัฒนาการของ Phantom ที่มีอีโก้ ตอนนี้มีความสามารถแยกร่าง",
'mysticism.race.fire_ant.description':"มดที่วิวัฒนาการแล้ว เน้นการโจมตี สามารถจุดไฟให้การโจมตีกายภาพ คล้ายเอ็นชานต์ Fire Aspect",
'mysticism.race.fire_ant_insectar.description':"Fire Ant ที่ได้ร่างมนุษย์ มันกัดต่อยอย่างเจ็บปวดและต่อสู้อย่างดุร้าย",
'mysticism.race.fire_ant_savant.description':"Fire Ant ที่วิวัฒนาการ \"อย่างถูกต้อง\" และกลายเป็นสิ่งมีชีวิตวิญญาณ มันปฏิบัติตามเจตจำนงของกองทัพ เป็นประภาคารที่ส่องสว่างสำหรับ Fire Ant ตัวอื่น",
'mysticism.race.flame_soul_insect.description':"Fire Ant ที่วิวัฒนาการ \"อย่างถูกต้อง\" และกลายเป็นสิ่งมีชีวิตวิญญาณ มันแทนธาตุ Flames ได้อย่างสมบูรณ์แบบ เผาศัตรูให้ตายอย่างเปลวเพลิง",
'mysticism.race.forgotten.description':"เผ่า Forgotten ดิ้นรนที่จะจดจำ ผี เงาของสิ่งที่เคยเป็น ซากวิญญาณของผู้ที่จากไปนาน ซึ่งนำไปเกิดใหม่ไม่ได้ ถูกทิ้งให้วนเวียนในโลกชั่วนิรันดร์",
'mysticism.race.frost_wolf.description':"Direwolf ที่มีความเชื่อมโยงกับน้ำแข็ง อุณหภูมิลดลงถึงจุดเยือกแข็งถึงตายเมื่อมีมันอยู่ใกล้",
'mysticism.race.frostcoil_sea_serpent.description':"เผ่ามังกรทะเลที่อาศัยอยู่ในส่วนลึกที่หนาวที่สุดของทุนดราแห่งมหาสมุทร ใช้หูที่ได้รับการเสริมหาเหยื่อ และใช้ความเร็วไล่จับ",
'mysticism.race.frostwrought_leviathan.description':"มังกรอันตรายที่อาศัยใกล้ก้นมหาสมุทร เผ่าที่เชื่องแต่อันตราย บิดเบือนเสียงเพื่อหาและจับภัยคุกคามได้",
'mysticism.race.gale_spirit_wolf.description':"สิ่งมีชีวิตที่น่ากลัวอย่างแท้จริง นี่คือ Direwolf ที่ \"วิวัฒนาการอย่างถูกต้อง\" และกลายเป็น Spiritual Lifeform แทบไม่มีกำเนิดขึ้นมาแม้สักครั้งในหนึ่งพันปี และ Direwolf กับ Black Fang ทั่วไปทุกตัวโค้งคำนับต่อสิ่งมีชีวิตนี้",
'mysticism.race.general.description':"ผู้บัญชาการของกองทัพ Phantom",
'mysticism.race.glacier_spirit_wolf.description':"สิ่งมีชีวิตที่น่ากลัวอย่างแท้จริง นี่คือ Direwolf ที่ \"วิวัฒนาการอย่างถูกต้อง\" และกลายเป็น Spiritual Lifeform แทบไม่มีกำเนิดขึ้นมาแม้สักครั้งในหนึ่งพันปี และ Direwolf กับ Frost Wolf ทั่วไปทุกตัวโค้งคำนับต่อสิ่งมีชีวิตนี้",
'mysticism.race.gravity_soul_insect.description':"WIP",
'mysticism.race.greater_angel.description':"วิวัฒนาการของ Lesser Angel ที่มีอีโก้พัฒนามากขึ้น",
'mysticism.race.greater_doll.description':"ผลของ Greater Daemon ที่สิงร่าง magisteel",
'mysticism.race.greater_elemental.description':"Elemental ที่วิวัฒนาการให้มีรูปร่างคล้ายมนุษย์มากขึ้น ระวังเวทวิญญาณระดับ Greater ที่ทรงพลังของมัน!",
'mysticism.race.greater_fallen.description':"Greater Angel ที่ถูกมาจิคูลทำให้เสื่อมทราม แล้วเลือกละทิ้งแสงสว่างเพื่อความมืด",
'mysticism.race.greater_glacier_wyrm.description':"วิวัฒนาการขั้นสูงของไวร์มที่อาศัยในทุนดราน้ำแข็ง ทรงพลังและอันตรายยิ่งกว่าวิวัฒนาการก่อนหน้า ใช้ลมหายใจน้ำแข็งแช่แข็งทุกผู้ที่พบมัน วิวัฒนาการขั้นสูงของไวร์มที่อาศัยในทุนดราน้ำแข็ง ทรงพลังและอันตรายยิ่งกว่าวิวัฒนาการก่อนหน้า ใช้ลมหายใจน้ำแข็งแช่แข็งทุกผู้ที่พบมัน",
'mysticism.race.greater_pyre_wyrm.description':"วิวัฒนาการขั้นสูงของไวร์มที่อาศัยในทะเลทราย ใช้ลมหายใจเพลิงเผาเหยื่อขณะล่าผู้ที่ไม่ได้เตรียมรับความร้อน",
'mysticism.race.green_fang.description':"Direwolf ที่มีความเชื่อมโยงกับลม "+SENSE,
'mysticism.race.guitar_wolf.description':"Direwolf ที่มีความเชื่อมโยงกับเสียง "+SENSE,
'mysticism.race.hardshell_ant.description':"มดที่วิวัฒนาการแล้ว เน้นการป้องกัน โดยธรรมชาติมีมวลดี ทำให้เอาออกจากการต่อสู้ยากมาก",
}
DIV="การปรากฏตัวเช่นนี้ดึงความสนใจของทุกคน โปรดระวังว่าคุณอาจไม่รอดกลับมาครบทุกส่วนเมื่อเผชิญ {n} ที่ได้รับ Divinity"
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    vv=json.loads(v)
    m=re.search(r'monster of an? (.+?) that has gained Divinity',vv)
    if m: out[k]=DIV.format(n=m.group(1)); continue
    if a in D and D[a] is not None: out[k]=D[a]
print('keys',len(keys),'out',len(out),[k.split('wiki.')[-1] for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
