import json,sys
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=80
S={
'snowflake':(None,"หกกิ่ง แต่ละกิ่งแตกแขนง"),
'flame':("เปลวไฟ","ลิ้นที่ชูขึ้นเป็นปลายแหลม"),
'wave_crest':("คลื่นแตก","คลื่นที่ม้วนทับตัวเอง"),
'rain_cloud':("เมฆฝน","เมฆที่มีเส้นตกลงมา"),
'grass':("หญ้า","ใบที่เอนไปตามลม"),
'mushroom':("เห็ด","โดมที่ตั้งบนก้าน"),
'cactus':("กระบองเพชร","ลำต้นที่ชูสองแขน"),
'tulip':("ทิวลิป","ถ้วยกลีบดอกบนก้าน"),
'clover':("โคลเวอร์","สี่วงกลมที่พบกันที่ก้าน"),
'apple':("แอปเปิล","วงกลมที่มีใบอยู่ด้านบน"),
'snail':("หอยทาก","ขดที่แบกไว้บนเท้ายาว"),
'spider_web':("ใยแมงมุม","รัศมีที่ผูกด้วยวงแหวน"),
'butterfly':("ผีเสื้อ","สี่ปีกจากลำตัวเดียว"),
'paw':("อุ้งเท้า","แผ่นรองที่มีสี่นิ้วเล็ก"),
'feather':("ขนนก","ก้านที่มีหนามทั้งสองข้าง"),
'volcano':("ภูเขาไฟ","ยอดที่ถูกตัดที่พุ่งขึ้นเบื้องบน"),
'palm':("ปาล์ม","ลำต้นที่โค้งใต้ใบห้อยย้อย"),
'lotus':("ดอกบัว","กลีบที่ชูขึ้นจากน้ำนิ่ง"),
'sunrise':("อรุณรุ่ง","ครึ่งวงกลมเหนือเส้นขอบฟ้า"),
'wheat':("ข้าวสาลี","ก้านที่หนักด้วยเมล็ด"),
'key':("กุญแจ","วงแหวนที่มีฟันบนก้าน"),
'sword':("ดาบ","ใบดาบยาวเหนือการ์ด"),
'bow_arrow':("ธนูที่น้าวสาย","ธนู สาย และลูกศร"),
'trident':("ตรีศูล","ก้านที่จบด้วยสามง่าม"),
'anchor':("สมอเรือ","ก้านที่มีตะขอทั้งสองข้าง"),
'axe':("ขวาน","หัวโค้งบนด้าม"),
'labrys':("ลาบริส","สองใบมีดโค้งหันหลังชนกัน"),
'hammer':("ค้อน","ก้อนที่วางขวางด้าม"),
'bell':("ระฆัง","ถ้วยที่บานออกพร้อมลิ้น"),
'lantern':("โคมไฟ","กรอบที่ห้อยจากด้าม"),
'candle':("เทียน","เสาที่มีเปลวไฟอยู่เหนือ"),
'chalice':("จอกศักดิ์สิทธิ์","ถ้วยบนก้านยาว"),
'jeweled_crown':("มงกุฎประดับอัญมณี","ยอดที่สวมอัญมณี"),
'scales':("ตราชั่ง","คานที่มีสองจานห้อย"),
'open_book':("หนังสือที่เปิด","สองหน้าจากสันเดียว"),
'house':("บ้าน","หลังคาเหนือสี่ผนัง"),
'tower':("หอคอย","ลำตัวสูงที่สวมกำแพงเชิงเทิน"),
'torii':("โทริอิ","สองเสาใต้คานโค้ง"),
'bridge':("สะพาน","ซุ้มโค้งที่รับถนน"),
'boat':("เรือ","ตัวเรือใต้ใบเรือ"),
'padlock':("แม่กุญแจ","ห่วงคล้องบนตัวที่ปิดสนิท"),
'scissors':("กรรไกร","สองห่วง สองใบมีดไขว้"),
'potion':("ยา","ขวดกลมคอแคบ"),
'scythe':("เคียวยาว","ด้ามยาวและใบมีดโค้งงอ"),
'umbrella':("ร่ม","โดมขอบหยักบนก้านที่เป็นตะขอ"),
'gem':("อัญมณี","หินเจียระไนที่มีเหลี่ยม"),
'fan':("พัด","ซี่ที่กางออกจากจุดเดียว"),
'crossed_swords':("ดาบไขว้","สองใบดาบไขว้กัน การ์ดแยกออก"),
'pickaxe':("พิคแอกซ์","หัวโค้งบนด้ามตรง"),
}
D={
'greatsage.ep1.kakutoku':"กำลังได้รับ…",
'greatsage.assess.alignment':"Alignment",
'greatsage.assess.mark.demon_lord_seed':"Demon Lord Seed",
'greatsage.assess.mark.true_demon_lord':"True Demon Lord",
'greatsage.assess.mark.hero_egg':"Hero Egg",
'greatsage.assess.mark.true_hero':"True Hero",
'greatsage.assess.mark.blessed':"ได้รับพร",
'greatsage.scene.glitch.banner':"เสียงแห่งโลก // สัญญาณขาด",
'greatsage.scene.glitch.trace':"ร่องรอย โลกจะตัดสินใจแทนเจ้า",
'greatsage.scene.glitch.imposed':"โลกได้ตัดสินใจแล้ว",
'greatsage.scene.glitch.accept':"กด Enter หรือคลิกเพื่อยอมรับ",
'greatsage.sense.on':"Magic Sense: เปิดใช้งานแล้ว",
'greatsage.sense.missing':"ประกาศ คุณไม่มีสกิลรับรู้ (Magic Sense, Universal Perception...)",
'greatsage.sense.ep':"EP %s",
'greatsage.skill.raphael':"Raphael, Lord of Wisdom",
'greatsage.whatsnew.title':"มีอะไรใหม่",
'greatsage.whatsnew.continue':"ดำเนินต่อ",
'greatsage.whatsnew.0_0_7.1.title':"การเรนเดอร์ด้วย shader: โฉมใหม่ของ Sage",
'greatsage.whatsnew.0_0_7.1.desc':"เปิดเป็นค่าเริ่มต้น คอนโซลของ Sage แทนที่เมนู และทุกการประกาศถูกวาดใหม่ ใช้ /gamerule sageShaderRendering false เพื่อคืนรูปลักษณ์แบบคลาสสิก",
'greatsage.whatsnew.0_0_7.2.title':"พิธีกรรมเป็นฉากจริง",
'greatsage.whatsnew.0_0_7.2.desc':"Harvest Festival, Demon Lord Seed, Hero Egg, True Hero และการตื่นรู้ True Demon Lord ตอนนี้เป็นฉากเต็มจอพร้อมบรรยากาศของตัวเอง ไม่มีสิ่งใดทำร้ายหรือผลักคุณได้ระหว่างที่เล่นอยู่",
'greatsage.whatsnew.0_0_7.3.title':"วิวัฒนาการของ Raphael สร้างใหม่",
'greatsage.whatsnew.0_0_7.3.desc':"สร้างใหม่ทีละช็อตจากตอนที่ 35",
}
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    if a in D: out[k]=D[a]; continue
    if a.startswith('greatsage.sigil.'):
        name=a.split('.')[2]
        t=S[name][1 if a.endswith('.reading') else 0]
        if t: out[k]=t
print('keys',len(keys),'out',len(out),[k.split('wiki.')[1] for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
