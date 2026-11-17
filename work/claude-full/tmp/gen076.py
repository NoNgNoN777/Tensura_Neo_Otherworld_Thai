import json,sys
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=76
D={
'greatsage.tree.needPoints':"ต้องการ %s แต้ม",
'greatsage.tree.nerve_1':"Cold blood I",
'greatsage.tree.nerve_1.desc':"เมื่อมันโจมตีคุณ มันจะโจมตีเบาลงหนึ่งขั้น",
'greatsage.tree.nerve_2':"Cold blood II",
'greatsage.tree.nerve_2.desc':"เบาลงสองขั้น การยืนใกล้สิ่งที่อยู่เหนือกว่าคุณมากไม่ทนไม่ได้อีกต่อไป",
'greatsage.tree.points':"%s แต้ม",
'greatsage.tree.rank_extra':"สกิล Extra",
'greatsage.tree.rank_extra.desc':"เปิดการฝึกสกิล Extra: ได้ความชำนาญ 1–2 ทุก 6 นาทีเมื่อจัดสรรเต็ม",
'greatsage.tree.rank_resistance':"ความต้านทาน",
'greatsage.tree.rank_resistance.desc':"การฝึกเป็นระยะไม่รองรับความต้านทาน โหนดนี้ไม่เปิดการวิเคราะห์ความต้านทานอีกต่อไป",
'greatsage.tree.rank_ultimate':"สกิล Ultimate",
'greatsage.tree.rank_ultimate.desc':"เปิดการฝึกสกิล Ultimate: ได้ความชำนาญ 1–2 ทุก 20 นาทีเมื่อจัดสรรเต็ม",
'greatsage.tree.rank_unique':"สกิล Unique",
'greatsage.tree.rank_unique.desc':"เปิดการฝึกสกิล Unique: ได้ความชำนาญ 1–2 ทุก 12 นาทีเมื่อจัดสรรเต็ม",
'greatsage.tree.reach_1':"Long sight I",
'greatsage.tree.reach_1.desc':"การประเมินไกลขึ้น 25%",
'greatsage.tree.reach_2':"Long sight II",
'greatsage.tree.reach_2.desc':"การประเมินไกลกว่าเดิม 75%",
'greatsage.tree.slot_2':"เธรดที่สอง",
'greatsage.tree.slot_2.desc':"วิเคราะห์สองสกิลพร้อมกัน ใช้งบเดียวกัน จึงให้ตัวเลือกเพิ่ม ไม่ใช่ความเร็ว",
'greatsage.tree.slot_3':"เธรดที่สาม",
'greatsage.tree.slot_3.desc':"สกิลที่สามถูกวิเคราะห์พร้อมกัน",
'greatsage.tree.slot_4':"เธรดที่สี่",
'greatsage.tree.slot_4.desc':"สกิลที่สี่ จำไว้ว่าทุกสกิลที่กำลังวิเคราะห์คือสกิลที่คุณใช้ไม่ได้",
'greatsage.tree.soon':"เร็วๆ นี้",
'greatsage.tree.soon.desc':"ยังได้รับไม่ได้ สิ่งที่มันจะกลายเป็นยังไม่ได้ตัดสินอย่างเปิดเผย",
'greatsage.tree.stomach_1':"Steady I",
'greatsage.tree.stomach_1.desc':"อาการป่วยเริ่มที่ 12 เท่าของ EP คุณ แทน 8 เท่า",
'greatsage.tree.stomach_2':"Steady II",
'greatsage.tree.stomach_2.desc':"อาการป่วยเริ่มที่ 18 เท่าของ EP คุณ",
'greatsage.tree.stomach_3':"Steady III",
'greatsage.tree.stomach_3.desc':"อาการป่วยเริ่มที่ 28 เท่าของ EP คุณ",
'greatsage.voice.kaiseki_kanryou':"ตอบ การฝึกวิเคราะห์เสร็จสมบูรณ์ สกิลชำนาญแล้ว",
'greatsage.voice.shinchoku':"รอบการวิเคราะห์ปัจจุบันของ %s เสร็จสมบูรณ์ %s",
'greatsage.scene.escape':"กด Escape อีกครั้งเพื่อเปิดหน้าจอการเกิดใหม่ของ Tensura",
'greatsage.tree.max':"เลเวลสูงสุด",
'greatsage.analysis.failed':"การวิเคราะห์ %s ล้มเหลว ไม่ได้เรียนรู้สิ่งใด",
'greatsage.analysis.failedRecovered':"การวิเคราะห์ %s ล้มเหลว กู้คืนมาจิคูลได้ %s",
'greatsage.analysis.efficiency':"การจัดสรร",
'greatsage.analysis.success':"+1–2 ต่อรอบ (%s%%)",
'greatsage.tree.branch.insight':"ความแม่นยำ",
'greatsage.tree.budget_4':"Focus IV",
'greatsage.tree.budget_4.desc':"ขยายสเกลการจัดสรรเป็น 140% รอบพื้นฐานที่การจัดสรรเต็มไม่เปลี่ยนแปลง",
'greatsage.tree.budget_5':"Focus V",
'greatsage.tree.budget_5.desc':"ขยายสเกลการจัดสรรเป็น 150% ไม่ทำให้รอบพื้นฐานสั้นลง ยังต้องมีเธรดที่สี่",
'greatsage.tree.reach_3':"Long sight III",
'greatsage.tree.reach_3.desc':"การประเมินไกลสองเท่าครึ่งของตอนเริ่มต้น",
'greatsage.tree.ceiling_4':"Deep read IV",
'greatsage.tree.ceiling_4.desc':"สูงสุด 60 เท่าของ EP คุณเอง ขีดจำกัดเลื่อนไป แต่ไม่หายไป",
'greatsage.tree.precision_1':"Precision I",
'greatsage.tree.precision_1.desc':"เดิมลดโอกาสวิเคราะห์ล้มเหลว 15% การฝึกเป็นระยะไม่มีการสุ่มล้มเหลว ผลนี้จึงไม่ทำงาน",
'greatsage.tree.precision_2':"Precision II",
'greatsage.tree.precision_2.desc':"เดิมลดโอกาสล้มเหลวที่เหลือ 20% การฝึกเป็นระยะไม่มีการสุ่มล้มเหลว ผลนี้จึงไม่ทำงาน",
'greatsage.tree.precision_3':"Precision III",
'greatsage.tree.precision_3.desc':"เดิมลดโอกาสล้มเหลวที่เหลือ 25% การฝึกเป็นระยะไม่มีการสุ่มล้มเหลว ผลนี้จึงไม่ทำงาน",
'greatsage.tree.precision_4':"Precision IV",
'greatsage.tree.precision_4.desc':"เดิมลดโอกาสล้มเหลวที่เหลือ 30% การฝึกเป็นระยะไม่มีการสุ่มล้มเหลว ผลนี้จึงไม่ทำงาน",
'greatsage.tree.precision_5':"Precision V",
'greatsage.tree.precision_5.desc':"เดิมลดโอกาสล้มเหลวที่เหลือ 40% การฝึกเป็นระยะไม่มีการสุ่มล้มเหลว ผลนี้จึงไม่ทำงาน",
'greatsage.tree.recovery':"Second look",
'greatsage.tree.recovery.desc':"การฝึกเป็นระยะไม่มีการสุ่มล้มเหลว จึงไม่มีการคืนมาจิคูลเมื่อวิเคราะห์ล้มเหลว",
'greatsage.word.north':"เหนือ",'greatsage.word.south':"ใต้",'greatsage.word.east':"ตะวันออก",'greatsage.word.west':"ตะวันตก",
'greatsage.word.above':"ด้านบน",'greatsage.word.below':"ด้านล่าง",'greatsage.word.rain':"ฝนตก",'greatsage.word.clear':"แจ่มใส",
'greatsage.word.fire':"ไฟ",'greatsage.word.not_fire':"ไม่ใช่ไฟ",'greatsage.word.yes':"ใช่",'greatsage.word.no':"ไม่ใช่",
'greatsage.word.dimension.overworld':"Overworld",'greatsage.word.dimension.the_nether':"Nether",'greatsage.word.dimension.the_end':"End",
}
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    if a in D: out[k]=D[a]
    elif a.startswith('greatsage.grant.'): out[k]=json.loads(v)
print('keys',len(keys),'out',len(out),[k for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
