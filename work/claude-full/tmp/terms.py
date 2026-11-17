import json,glob,re,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
texts=[]
for f in glob.glob(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\translation-src\lang\*\lang\th_th.json'):
    texts+= [v for v in json.load(open(f,encoding='utf-8')).values() if isinstance(v,str)]
q=json.load(open(r'D:\minecraft\Tensura_Neo_Otherworld_Thai\translation-src\quests\translations.json',encoding='utf-8'))['items']
for v in q.values(): texts+= v if isinstance(v,list) else [v]
big='\n'.join(texts)
groups={
 'magicule':['มาจิคูล','มาจิกูล','แมจิคูล','เมจิคูล','Magicule','มาจิคุล'],
 'skill':['สกิล','ทักษะ','ความสามารถ'],
 'demon lord':['จอมมาร','ราชาปีศาจ','Demon Lord','เดมอนลอร์ด'],
 'hero':['ผู้กล้า','ฮีโร่','Hero'],
 'reincarnat':['เกิดใหม่','กลับชาติมาเกิด','เกิดใหม่ชาติ','รีอินคาร์เนต'],
 'evolve':['วิวัฒนาการ','พัฒนาร่าง','ก้าวหน้าเป็น'],
 'resist':['ความต้านทาน','ต้านทาน','ภูมิต้านทาน','ความทนทาน'],
 'mastery':['ความชำนาญ','ความเชี่ยวชาญ','ชำนาญ','เชี่ยวชาญ'],
 'aura':['ออร่า','Aura','ปราณ'],
 'dwarf':['ดวอร์ฟ','ดาร์ฟ','คนแคระ','Dwarf'],
 'goblin':['ก็อบลิน','โกบลิน'],
 'ogre':['โอเกอร์','โอก','ออร์ก','Ogre'],
 'boss':['บอส','Boss'],
 'cooldown':['คูลดาวน์','ระยะคูลดาวน์','เวลาฟื้นตัว'],
 'durability':['ความทนทาน','ค่าความทนทาน','ความคงทน'],
 'enchant':['เอนชานต์','เอ็นชานต์','มนตร์เสริม','การร่ายเวทเสริม','เสริมเวท'],
 'villager':['ชาวบ้าน','วิลเลเจอร์'],
 'quest':['เควสต์','เควส','ภารกิจ'],
}
for g,ws in groups.items():
    print(g,{w:big.count(w) for w in ws})
