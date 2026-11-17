import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=86
T='tooltip.kaleidoscope_cookery.'
M={
'flower_tea':"ชาดึงกลิ่นหอมของดอกไม้ออกมา ดอกไม้ทำให้ชาอุดมสมบูรณ์",
'tieguanyin':"หนึ่งในสิบชาเลื่องชื่อของจีน สง่างามและหอมนานไม่จาง",
'barley_tea':"กลิ่นธัญพืชคั่วและจิบแล้วอบอุ่นนุ่มนวล",
'biluochun':"รูปทรงเกลียว เย็นหวานในปาก เคยถูกจัดเป็นชาเครื่องบรรณาการ",
'oolong':"กำเนิดในยุคซ่งเหนือ หอมเข้มข้นและกลมกล่อม",
'sakura_fubuki':"กลิ่นหอมสดชื่นพร้อมความลึกหลายชั้น",
'braised_beef_with_potatoes':"มันฝรั่งนุ่มและเนื้อวัวนุ่มละมุน",
'spicy_chicken':"ไก่ชา เผ็ด และหอม วิญญาณแห่งอาหารเสฉวน",
'nether_style_sashimi':"ซาชิมิกรอบรสเผ็ดร้อนหนึ่งจาน",
'dark_cuisine':"(โอ้โห อร่อยจัง! *อาเจียน*)",
'sweet_and_sour_ender_pearls':"เปรี้ยวหวาน พร้อมไข่มุกที่ระเบิดในปาก!",
'beef_noodle':"เส้นเหนียวนุ่มกับเนื้อวัว อิ่มเอมล้นใจในชามเดียว",
'fish_flavored_shredded_pork':"ไม่มีปลาแต่เต็มไปด้วยกลิ่นปลา มนตร์วิเศษของอาหารเสฉวน",
'suspicious_stir_fry':"นี่มัน... เจ้ากำลังทำอาหารอะไรอยู่...!?",
'meat_pie':"เปลือกกรอบกับไส้เนื้อแน่นๆ",
'shengjian_mantou':"เซิงเจียนมันโถวกรอบหอม",
'dumpling':"แป้งบางเฉียบ ไส้แน่น น้ำซุปแตกในปาก รสชาติของบ้าน",
'braised_beef':"ซอสเข้มข้นหอมกรุ่น เนื้อละเอียดนุ่ม",
'chicken_and_mushroom_stew':"ไก่ตุ๋นกับเห็ด หอมอย่างไม่น่าเชื่อ",
'samsa':"ขนมอบดั้งเดิมของซินเจียง",
'cold_style_sashimi':"ซาชิมิกรอบสดชื่นหนึ่งจาน",
'mantou':"ซาลาเปาไร้ไส้ที่อวบอิ่มขาวดั่งหิมะ",
'chorus_fried_egg':"รสชาติแบบ End หอมกรุ่น",
'tundra_style_sashimi':"ซาชิมิสดหนึ่งจานพร้อมกลิ่นมอส",
'fondant_spider_eye':"ความหวาดกลัวที่ห่อด้วยน้ำตาล อาหารมืดหวาน",
'pork_bone_soup':"หอม กรุ่น อิ่มและมีประโยชน์",
'egg_fried_rice':"เม็ดข้าวร่วน สีและรสยอดเยี่ยม",
'hui_noodle':"เส้นหุ้ยเหนียวนุ่มในน้ำซุปเข้มข้น รสชาติแห่งที่ราบภาคกลาง",
'lamb_and_radish_soup':"เนื้อแกะนุ่ม หัวไชเท้ารสกลมกล่อม",
'seafood_miso_soup':"ตัวเลือกอ่อนๆ ที่อุ่นท้อง",
'crystal_lamb_chop':"ซี่โครงแกะใสดั่งคริสตัล",
'stir_fried_pork_with_peppers':"พริกเขียวกรอบและเนื้อหมูหั่นบางนุ่ม",
'slime_ball_meal':"กินข้าวสไลม์สักชาม แล้วติดกันแน่นคืนนี้!",
'fearsome_thick_soup':"ซุปข้นนี้ช้อนเดียวทำให้โลกห้อยลู่",
'pufferfish_soup':"อันดับหนึ่งในสามอาหารอันโอชะแห่งแยงซี สดที่สุดเมื่อฤดูใบไม้ผลิทำให้แม่น้ำอุ่น",
'golden_salad':"ชุดสลัดสุดหรูหราไม่มีใครเทียบ",
'baozi':"เปาจื่อร้อนฉ่า",
'qingtuan':"ขนมเทศกาลเช็งเม้งนึ่งจากน้ำโกฐจุฬาลัมพาและแป้งข้าวเหนียว",
'sticky_candy':"ขนมหวานเหนียวนุ่มทำจากน้ำตาลและงา",
'sticky_rice_cake':"สัญลักษณ์ของการเก็บเกี่ยวและการกลับมาพบกันในวัฒนธรรมและเทศกาลฮักกา\nมักกินในเทศกาลฉงหยางและวันหยุดอื่นๆ",
'zongzi':"อาหารเทศกาลเรือมังกรที่เล่ากันว่าระลึกถึงกวีฉู่ยฺเหวียน",
'raw_bamboo_tube_rice':"อาหารดั้งเดิมของจีนตอนใต้ ทำโดยบรรจุข้าวหอม ข้าวเหนียว เนื้อ และผัก\nลงในกระบอกไม้ไผ่ก่อนปรุงสุก",
'bamboo_tube_rice':"อาหารดั้งเดิมของจีนตอนใต้ ทำโดยบรรจุข้าวหอม ข้าวเหนียว เนื้อ และผัก\nลงในกระบอกไม้ไผ่ก่อนปรุงสุก",
'hot_dry_noodles':"เส้นด่างคลุกน้ำพริกงาและเครื่องปรุง\nสีเหลือง มันวาว รสเค็มกลมกล่อม และเป็นหนึ่งในของว่างที่มีชื่อเสียงที่สุดของอู่ฮั่น",
'laba_congee':"ของว่างเทศกาลลาป๋าที่เคี่ยวจากธัญพืชและถั่ว",
'scramble_egg_with_tomatoes_rice_bowl':"มะเขือเทศผัดไข่หนึ่งช้อนราดข้าว ความสุขล้นปรี่",
'borscht':"เปรี้ยวหวาน เจริญอาหาร ปีติสุขลอยฟ้า",
'sweet_and_sour_pork':"กรอบนอกนุ่มใน เปรี้ยวหวาน",
'stir_fried_pork_with_peppers_rice_bowl':"ข้าวเคลือบซอส อิ่มเอมทุกคำ",
'donkey_burger':"เนื้อมังกรบนสวรรค์ เนื้อลาบนดิน",
'fish_flavored_shredded_pork_rice_bowl':"หมูหั่นฝอยนุ่มพร้อมกลิ่นเห็ดสด",
'cooked_rice':"ใครจะรู้ว่าทุกเม็ดบนจานมาจากความเหนื่อยยาก?",
'desert_style_sashimi':"ซาชิมิแห้งกรอบแบบทรายหนึ่งจาน",
'scramble_egg_with_tomatoes':"หวาน เปรี้ยว และนุ่ม อาหารปลอบใจประจำตัว",
'udon_noodle':"เส้นอุด้งเด้งนุ่ม น้ำซุปเข้มข้นอร่อย",
'dongpo_pork':"\"ไม่มีเนื้อ คนจะผอม ไม่มีไผ่ คนจะหยาบ\"",
'wild_mushroom_rabbit_soup':"กระต่ายนุ่มกับเห็ดสดหอม",
'beef_meatball_soup':"เกิดมากับชาวฮักกา สมบูรณ์แบบที่เฉาซ่าน กัดแล้วน้ำซุปแตก",
'braised_beef_rice_bowl':"อาหารวิญญาณของคนรักข้าว",
'frost_lamb_chop':"ซี่โครงแกะเย็นลื่นนุ่ม",
'sweet_and_sour_pork_rice_bowl':"หมูเปรี้ยวหวานเข้ากับข้าวมาก ช่วยให้อารมณ์ดีแน่นอน",
'stargazy_pie':"ปลาแหงนมองฟ้า ราวกับจมอยู่ในความคิด",
'blaze_lamb_chop':"ซี่โครงแกะเผ็ด ชา และเค็มกลมกล่อม",
'fondant_pie':"พายฟักทองห่อน้ำผึ้งหวาน ผลงานศิลปะแห่งโลกของหวาน",
'end_style_sashimi':"ซาชิมิเย็นเด้งหนึ่งจาน",
'pan_seared_knight_steak':"แหล่งพลังของอัศวินเอง",
'candied_potato':"เส้นน้ำตาลยาวและกลิ่นมันฝรั่งเต็มที่",
'dough_drop_soup':"ซุปพื้นบ้านที่พบทั่วไปในจีนตอนเหนือ",
'stuffed_tiger_skin_pepper':"พริกเขียวทอดจนเป็นลายหนังเสือ ห่อไส้เนื้อรสเค็มฉ่ำ",
'spicy_rabbit_head':"เจ้ากินกระต่ายน้อยได้ยังไง!",
'four_joy_meatball_soup':"ลูกชิ้นกลมที่แช่ในน้ำซุปเข้มข้น สดและกลมกล่อม",
'numbing_spicy_chicken':"อาหารเลิศรสของซินเจียงที่ไก่ฉีกชัดเจนและกัดแล้วชาสดชื่น",
'fried_caterpillar':"โปรตีนกรุบกรอบ!",
'fried_spring_roll':"ทอดด้วยไฟอ่อน เหลืองทอง กรอบและนุ่ม\nเล่ากันว่าวิวัฒนาการมาจาก \"แพนเค้กฤดูใบไม้ผลิ\" ของราชวงศ์จิ้นตะวันออก",
'spicy_blood_stew':"เผ็ดเผ็ดเผ็ดเผ็ดเผ็ดเผ็ดเผ็ดเผ็ดเผ็ด!",
'brown_mushroom_pot_soup':"หม้อซุปอุ่นๆ",
'red_mushroom_pot_soup':"หม้อซุปอุ่นๆ",
'warped_fungus_pot_soup':"หม้อซุปที่มีรสชาติเฉพาะตัว",
'crimson_fungus_pot_soup':"หม้อซุปที่มีรสชาติเฉพาะตัว",
'buddha_jumps_over_the_wall':"สีน้ำตาลมันวาว นุ่มและเข้มข้น ข้นแต่ไม่เลี่ยน\nอาหารพิเศษอันโด่งดังของฝูเจี้ยน",
'braised_pork_ribs':"หมูซี่โครงนุ่มหลุดจากกระดูกพร้อมซอสเข้มข้น",
'cold_roasted_meat':"จานเนื้อนุ่มหั่นบางละเอียด",
'oil_splashed_fish':"ราดน้ำมันร้อนให้กลิ่นหอมพวยพุ่ง\nพร้อมรักษาปลาให้สดและนุ่ม\nเต็มไปด้วยความเผ็ดชา",
}
D={
'tooltip.kaleidoscope_cookery.sickle':"คลิกขวาเพื่อเก็บเกี่ยวพืชผลและกำจัดวัชพืช",
'tooltip.kaleidoscope_cookery.chance':"โอกาส %s",
'kaleidoscope_cookery.ponder.stockpot.header':"ทำอาหารด้วยหม้อต้มซุป",
'kaleidoscope_cookery.ponder.stockpot.text_1':"หากจะทำอาหารด้วยหม้อต้มซุป ให้วางบนแหล่งความร้อนที่ใช้ได้",
'kaleidoscope_cookery.ponder.stockpot.text_2':"ก่อนอื่น เติมน้ำซุปพื้นฐานลงในหม้อต้มซุป",
'kaleidoscope_cookery.ponder.stockpot.text_3':"จากนั้นเติมวัตถุดิบที่ต้องการ",
'kaleidoscope_cookery.ponder.stockpot.text_4':"หลังเติมวัตถุดิบที่ต้องการครบแล้ว ปิดหม้อต้มซุปด้วยฝาหม้อต้มซุป",
'kaleidoscope_cookery.ponder.stockpot.text_5':"แล้วรอสักครู่...",
'kaleidoscope_cookery.ponder.stockpot.text_6':"...แล้วเปิดฝาออก",
'kaleidoscope_cookery.ponder.stockpot.text_7':"อาหารพร้อมแล้ว!",
'kaleidoscope_cookery.ponder.pot.header':"ทำอาหารด้วยกระทะ",
'kaleidoscope_cookery.ponder.pot.text_1':"หากจะทำอาหารด้วยกระทะ ให้วางบนแหล่งความร้อนที่ใช้ได้",
'kaleidoscope_cookery.ponder.pot.text_2':"ก่อนอื่น เติมน้ำมันลงในกระทะ",
'kaleidoscope_cookery.ponder.pot.text_3':"จากนั้นเติมวัตถุดิบที่ต้องการ",
'kaleidoscope_cookery.ponder.pot.text_4':"หลังเติมวัตถุดิบที่ต้องการครบแล้ว ใช้พลั่วครัวเริ่มผัดได้เลย!",
'kaleidoscope_cookery.ponder.pot.text_5':"จากนั้น หลังผัดพอและรอสักครู่...",
'kaleidoscope_cookery.ponder.pot.text_6':"...อาหารก็เสร็จ!",
'kaleidoscope_cookery.ponder.steamer.header':"การวางซึ้งนึ่ง",
'kaleidoscope_cookery.ponder.steamer.text_1':"หากจะทำอาหารด้วยซึ้งนึ่ง ให้วางบนแหล่งความร้อนที่ใช้ได้",
'kaleidoscope_cookery.ponder.steamer.text_2':"จากนั้น วางซึ้งนึ่งเพิ่มบนอันที่มีอยู่เพื่อซ้อนให้สูงขึ้น...",
'kaleidoscope_cookery.ponder.steamer.text_3':"...และสูงขึ้นไปอีก!",
'kaleidoscope_cookery.ponder.steamer.text_4':"อย่างไรก็ตาม แหล่งความร้อนหนึ่งแหล่งให้ความร้อนได้แก่ซึ้งนึ่งสูงสุด 8 อัน...",
'kaleidoscope_cookery.ponder.steamer.text_5':"...ดังนั้น ระวังขีดจำกัดของมันด้วย!",
'kaleidoscope_cookery.ponder.steamer_1.header':"ทำอาหารด้วยซึ้งนึ่ง",
'kaleidoscope_cookery.ponder.steamer_1.text_1':"ใส่วัตถุดิบลงในซึ้งนึ่งจากด้านบน",
'kaleidoscope_cookery.ponder.steamer_1.text_2':"ซึ้งนึ่งที่มีวัตถุดิบอยู่แล้วก็ซ้อนกันได้โดยตรง",
'kaleidoscope_cookery.ponder.steamer_1.text_3':"หลังวางแล้ว คลิกขวาเพื่อปิดซึ้งนึ่งและเริ่มนึ่ง",
}
PL={'baozi_plate':'baozi','qingtuan_plate':'qingtuan','sticky_candy_plate':'sticky_candy','sticky_rice_cake_plate':'sticky_rice_cake','zongzi_plate':'zongzi'}
PLT={'berry_platter':"ถาดผลเบอร์รีหวานสด",'apple_platter':"ถาดแอปเปิลสีแดงระเรื่อ",'tomato_platter':"ถาดมะเขือเทศสด",'watermelon_platter':"ถาดแตงโมหั่นชิ้น",'chorus_fruit_platter':"ถาดผลคอรัสลึกลับ"}
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    if a in D: out[k]=D[a]; continue
    m=re.fullmatch(re.escape(T)+r'(\w+)\.maxim',a)
    if m and m.group(1) in M: out[k]=M[m.group(1)]; continue
    m=re.fullmatch(re.escape(T)+r'(\w+)',a)
    if m:
        n=m.group(1)
        if n in PL: out[k]=M[PL[n]]
        elif n in PLT: out[k]=PLT[n]
print('keys',len(keys),'out',len(out),[k.split('wiki.')[-1] for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
