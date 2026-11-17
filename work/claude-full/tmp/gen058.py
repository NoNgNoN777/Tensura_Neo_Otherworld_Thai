import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
keys=[l.split(' = ',1)[0] for l in open(W+r'\tmp\d058.txt',encoding='utf-8').read().split('\n') if ' = ' in l]
T={}
S='foxablazeaqzl_wiki.wiki.'
TAIL=" เปิดผ่านเมนูวิวัฒนาการ ultimate ขึ้นอยู่กับการตั้งค่าวิวัฒนาการ ความจุมาจิคูล และช่อง ultimate"
d5="ชำนาญการแปลงร่างธาตุที่ตรงกันและมี EP ตามเกณฑ์การแปลงร่างธาตุเวทที่ตั้งค่าไว้"
for k in keys:
    if re.search(r'magic_(space|water|wind)_transform',k):T[k]=d5
    elif k.endswith('_nullification.description') and 'evolution.tensura.' in k:
        T[k]="ระหว่างการตื่นรู้เป็น Hero หรือ Demon Lord ความต้านทานที่ได้รับถาวรอาจวิวัฒนาการเป็น nullification ที่จับคู่ไว้ การชำนาญเพียงอย่างเดียวไม่กระตุ้นสิ่งนี้ การเรียนรู้และ game rule มีผลด้วย"
E={
'evolution.tensura.black_flame':"เงื่อนไขรวม: มี Black Lightning และ Molecular Manipulation และชำนาญ Flame Transform",
'evolution.tensura.thermal_fluctuation_resistance':"ต้องมี (Cold Resistance หรือ Cold Nullification) และ (Heat Resistance หรือ Heat Nullification) การได้รับฝั่งหนึ่งจะตรวจอีกฝั่งและให้ Thermal Fluctuation Resistance",
'evolution.tensura.farsight':"การชำนาญเวท Clairvoyance เป็นหนึ่งในเส้นทางการได้รับ Farsight เงื่อนไข EP ที่ตั้งค่าไว้เป็นทางเลือกอื่น",
'evolution.tensura.analytical_appraisal':"การชำนาญเวท Analyze เป็นหนึ่งในเส้นทางการได้รับ Analytical Appraisal เงื่อนไข EP ที่ตั้งค่าไว้เป็นทางเลือกอื่น",
'evolution.tensura.body_double':"มี EP ตามเกณฑ์ Body Double และชำนาญเวท Doppelganger การเอาชนะ Ifrit เป็นทางเลือกแทนเงื่อนไขการชำนาญเวท",
'evolution.tensura.possession':"ชำนาญเวท Possession เพื่อให้ตรงตามเงื่อนไขการได้รับสกิล Possession",
'evolution.mortal_cultivation.great_sage.recipe.mortal_cultivation.great_sage_evolution':"ชำนาญ Mischief ถึง 1000 และสะสมบันทึกวิวัฒนาการ: ระเบิด 100 ครั้ง กิน golden apple 20 ลูก (รวม enchanted) และเคลื่อนที่ 500000 บล็อก วิวัฒนาการจะแทนที่ Mischief ด้วย Great Sage",
'evolution.trnightmare.beelzebuth.recipe.trnightmare.ultimate_beelzebuth':"ชำนาญ Gluttony และ Merciless จากนั้นตรงตามเงื่อนไขจำนวนการสังหารมอนสเตอร์ จำนวนชิ้นเค้ก และพลังชีวิตต่ำที่ตั้งค่าไว้",
'evolution.trnightmare.lucifer.recipe.trnightmare.ultimate_lucifer':"เรียนรู้ Pride และตรงตามเงื่อนไขจำนวนสกิลที่ชำนาญและพลังชีวิตต่ำที่ตั้งค่าไว้",
'evolution.trnightmare.asmodeus.recipe.trnightmare.ultimate_asmodeus':"ชำนาญสกิลที่เป็นเงื่อนไขและตรงตามจำนวนผู้ใต้บังคับบัญชาที่ตั้งชื่อและจำนวนการผสมพันธุ์สัตว์ที่ตั้งค่าไว้",
'evolution.trnightmare.satanael.recipe.trnightmare.ultimate_satanael':"ชำนาญสกิลที่เป็นเงื่อนไขและตรงตามเงื่อนไข Hero of the Village จำนวนการสังหารมอนสเตอร์ และพลังชีวิตต่ำที่ตั้งค่าไว้",
'evolution.trnightmare.mammon.recipe.trnightmare.ultimate_mammon':"ชำนาญ Greed ตรงตามจำนวนการแลกเปลี่ยนกับชาวบ้านและ Hero of the Village ที่ตั้งค่าไว้ และพกบล็อกทองที่ต้องการ",
'evolution.trnightmare.leviathan.recipe.trnightmare.ultimate_leviathan':"ชำนาญสกิลที่เป็นเงื่อนไขและตรงตามจำนวน Hero of the Village ที่ตั้งค่าไว้",
'evolution.trnightmare.gabriel.recipe.trnightmare.ultimate_gabriel':"ชำนาญ Cadence และตรงตามจำนวน Hero of the Village และจำนวนการใช้ time-freeze ที่ตั้งค่าไว้",
'evolution.trnightmare.yaoyorozu.recipe.trnightmare.ultimate_yaoyorozu':"เรียนรู้ Analyst และ Manufacturer เมื่อมีในเวอร์ชันนี้ ชำนาญอย่างน้อย 100 สกิลและ 40 ความสามารถเวท และชนะ raid สามครั้ง",
'evolution.trnightmare.cthulhu.recipe.trnightmare.ultimate_cthulhu':"ชำนาญทั้งสองเงื่อนไข ตรงตามจำนวนการสังหารมอนสเตอร์ที่ตั้งค่าไว้ และมีเลเวลเอฟเฟกต์ Insanity ที่ต้องการ",
'evolution.trnightmare.raphael_knowledge.recipe.trnightmare.ultimate_raphael_knowledge':"ชำนาญ Great Sage และตรงตามจำนวนสกิลที่ชำนาญ Hero of the Village และผู้ใต้บังคับบัญชาที่ตั้งชื่อที่ตั้งค่าไว้",
'evolution.trnightmare.raphael_wisdom.recipe.trnightmare.ultimate_raphael_wisdom':"ชำนาญ Great Sage และ Degenerate และตรงตามจำนวนสกิลที่ชำนาญ Hero of the Village และผู้ใต้บังคับบัญชาที่ตั้งชื่อที่ตั้งค่าไว้",
'evolution.trnightmare.uriel_lord_of_vow.recipe.trnightmare.ultimate_uriel_lord_of_vow':"ชำนาญ Infinity Prison และตรงตามจำนวน Hero of the Village และผู้ใต้บังคับบัญชาที่ตั้งชื่อที่ตั้งค่าไว้",
'evolution.trnightmare.merlin.recipe.trnightmare.ultimate_merlin':"ชำนาญ Infinity เรียนรู้ Sage และ Forbidden Knowledge และตรงตามจำนวนเวทที่ชำนาญและจำนวนเวทที่ Infinity คัดลอกที่ตั้งค่าไว้",
'evolution.trnightmare.amaterasu.recipe.trnightmare.ultimate_amaterasu':"ชำนาญเงื่อนไขทั้งหมดของสูตรและตรงตามจำนวนผู้ใต้บังคับบัญชาที่ตั้งชื่อและพลังชีวิตต่ำที่ตั้งค่าไว้",
'evolution.trnightmare.haniel.recipe.trnightmare.ultimate_haniel':"ชำนาญสกิลที่เป็นเงื่อนไขและตรงตามจำนวน Hero of the Village และค่าเกราะที่ตั้งค่าไว้",
'evolution.trnightmare.susanoo.recipe.trnightmare.ultimate_susanoo':"ชำนาญสกิลที่เป็นเงื่อนไขและตรงตามจำนวนการสังหารมอนสเตอร์และจำนวนสกิลที่ชำนาญที่ตั้งค่าไว้",
'evolution.trnightmare.astraea.recipe.trnightmare.ultimate_astraea':"ชำนาญ Gift และตรงตามจำนวนการสังหารมอนสเตอร์ สกิลที่ชำนาญ Hero of the Village และผู้ใต้บังคับบัญชาที่ตั้งชื่อที่ตั้งค่าไว้",
'evolution.trnightmare.zehirete.recipe.trnightmare.ultimate_zehirete':"ชำนาญ Astraea และ Hero Haki และเรียนรู้ Hero Banner Blessing มี EP ปัจจุบันอย่างน้อย 30,000,000 และทำบททดสอบสังหารมังกรหนึ่งครั้ง ล้มปีศาจหนึ่งครั้ง และความอดทนของฟีนิกซ์สิบครั้ง",
'evolution.trnightmare.astral_light.recipe.trnightmare.ultimate_astral_light_mammon':"ชำนาญ Creator, Law Manipulation และ Mammon และตรงตามเงื่อนไขความจุมาจิคูลที่ตั้งค่าไว้",
'evolution.trnightmare.astral_light.recipe.trnightmare.ultimate_astral_light_anti_skill':"ชำนาญ Creator และ Law Manipulation เป็นมนุษย์หรือมีลักษณะวิญญาณ Esper เกินจำนวนการสร้าง Anti-Skill ที่ตั้งค่าไว้ และตรงตามเงื่อนไขความจุมาจิคูล",
'evolution.trnightmare.akashic_records.recipe.trnightmare.ultimate_akashic_records':"ชำนาญ Astral Light พกไอเทมความทรงจำที่ถูกต้อง ทำเงื่อนไข Byakko ของมันให้สำเร็จ และตรงตามเงื่อนไข EP ปัจจุบันและความจุมาจิคูลที่ตั้งค่าไว้",
'evolution.trnightmare.hastur.recipe.trnightmare.ultimate_hastur':"ชำนาญเงื่อนไขทั้งหมดของสูตรและตรงตามจำนวนสกิลที่ชำนาญและผู้ใต้บังคับบัญชาที่ตั้งชื่อที่ตั้งค่าไว้ เส้นทางเมนูนี้คงเงื่อนไขไว้",
'evolution.trnightmare.michael.recipe.trnightmare.ultimate_michael':"ชำนาญ Dominator และตรงตามจำนวน Hero of the Village และการสังหารมอนสเตอร์ที่ตั้งค่าไว้",
'evolution.trnightmare.sariel.recipe.trnightmare.ultimate_sariel':"ชำนาญ Unyielding และตรงตามจำนวน Hero of the Village ผู้ใต้บังคับบัญชาที่ตั้งชื่อ และการสังหารมอนสเตอร์ที่ตั้งค่าไว้",
'evolution.trnightmare.yog_sothoth.recipe.trnightmare.ultimate_yog_sothoth':"ชำนาญ Usurper, Infinity Prison และ Absolute Severance การเปิดใช้ Time Traveler ต้องเกินเกณฑ์ที่ตั้งค่าไว้",
'evolution.trnightmare.agni.recipe.trnightmare.ultimate_agni':"เรียนรู้ Raguel และชำนาญ Flame Domination, Flame Manipulation และ Heat Wave อยู่ใน Nether และตรงตามจำนวนการกิน blaze powder ที่ตั้งค่าไว้",
'evolution.trnightmare.galatine.recipe.trnightmare.ultimate_galatine':"ชำนาญ Sunshine ตื่นรู้เป็น True Hero มีเผ่าศักดิ์สิทธิ์ ตรงตามเงื่อนไข EP สูงสุดที่ตั้งค่าไว้ และสังหาร True Demon Lord หนึ่งตัว",
}
for k,v in E.items():
    kk=S+k+'.description'
    T[kk]=v+('' if k.startswith(('evolution.tensura','evolution.mortal')) else ('.'+TAIL if True else ''))
T[S+'evolution.trnightmare.raguel.recipe.trnightmare.ultimate_raguel.description']="ชำนาญ Endorse และตรงตามจำนวน Hero of the Village และ zombie villager ที่รักษาแล้วที่ตั้งค่าไว้ เปิดวิวัฒนาการอัตโนมัติ ultimate ของ Nightmare และวิวัฒนาการของสกิลนี้ และตรงตามเงื่อนไขความจุมาจิคูลและช่อง ultimate ต้องเรียนรู้อย่างเป็นทางการหลังปลดล็อก"
T[S+'evolution.trnightmare.cthugha.recipe.trnightmare.ultimate_cthugha.description']="ชำนาญ Raguel และตรงตามเงื่อนไขความจุมาจิคูลและการเอาชนะ Masayuuki ที่ตั้งค่าไว้เพื่อวิวัฒนาการอัตโนมัติ เส้นทางนี้แทนที่ Raguel เปิดวิวัฒนาการอัตโนมัติ ultimate ของ Nightmare และวิวัฒนาการของสกิลนี้ และตรงตามเงื่อนไขความจุมาจิคูลและช่อง ultimate ต้องเรียนรู้อย่างเป็นทางการหลังปลดล็อก"
# fix: the generic TAIL appended with a leading '.' then space; normalise
for k,v in list(T.items()):
    T[k]=v.replace('. เปิดผ่านเมนู','. เปิดผ่านเมนู')
miss=[k for k in keys if k not in T]
print('keys',len(keys),'T',len(T),'missing',[m.split('wiki.')[1] for m in miss])
tail={S+k.split('wiki.')[1]:v for k,v in T.items()}
json.dump({k[len(S):] if False else k:v for k,v in T.items()},open(W+r'\tmp\t058.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
