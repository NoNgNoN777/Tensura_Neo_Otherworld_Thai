"""Audit every cached namespace without the old key selection filter.

Reuse exact-source translation memory only. Keep all unmatched candidates visible.
"""
from pathlib import Path
import json,re,importlib.util,collections
R=Path(__file__).resolve().parent.parent
SKILL=R.parent/'modpack-thai-translator'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 sp=importlib.util.spec_from_file_location('mtt',SKILL/'scripts/mtt.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
 cache=read(R/'work/v113c/cache/lang_sources.json');manual=dict(zip([
 'menu.skill_intro','menu.adventure_archive','menu.item_archive','placeholder','evolution.title','evolution.toggle','evolution.or','evolution.all','evolution.reference','evolution.any_route','evolution.route_number',
 'wiki.item_category.consumables','wiki.item_section.raw','wiki.item_section.cooked','wiki.item_section.drinks','wiki.item_section.misc','wiki.item_category.mob_drops','wiki.item_section.magic_crystals','wiki.item_section.monster_leather','wiki.item_section.specific_mob_drops','wiki.item_section.essence','wiki.item_section.blood','wiki.item_category.schematics','wiki.item_category.misc','wiki.item_section.unprocessed','wiki.item_section.ingots','wiki.item_section.plants','wiki.item_section.elemental','wiki.item_section.core','wiki.item_section.shard','wiki.item_section.bone_golems','wiki.item_section.reset_scrolls','wiki.item_category.bosses','wiki.item_section.combat_mechanics'],[
 'คลังความสามารถ','บันทึกการผจญภัย','คลังข้อมูลไอเทม','ยังไม่มีคำอธิบายในต้นฉบับ','วิวัฒนาการสกิล · ลากเพื่อเลื่อน / เลื่อนล้อเมาส์เพื่อซูม','แสดง / ซ่อนเส้นทางวิวัฒนาการสกิล','หรือ','ต้องมีร่วมกัน','สกิลเดียวกันนี้แสดงไว้เพื่อระบุเงื่อนไขที่ต้องมี ไม่จำเป็นต้องรับสกิลซ้ำอีกครั้ง','เส้นทางใดก็ได้','เส้นทาง %s',
 'ของใช้สิ้นเปลือง','อาหารดิบ','อาหารปรุงสุก','เครื่องดื่ม','เบ็ดเตล็ด','ของดรอปจากม็อบ','Magic Crystals','Monster Leather','ของดรอปจากม็อบเฉพาะชนิด','Essence','เลือด','พิมพ์เขียว','เบ็ดเตล็ด','ยังไม่แปรรูป','แท่งโลหะ','พืช','ธาตุ','แกน','เศษชิ้นส่วน','Bone Golems','Reset Scrolls','บอส','กลไกการต่อสู้']))
 added=[];pending=[];excluded=collections.Counter()
 for ns,en in cache['en'].items():
  p=R/'translation-src/lang'/ns/'lang/th_th.json'
  if not p.exists():continue
  th=read(p);memory={}
  for path in [SKILL/'memory/mods'/(ns+'.json'),SKILL/'memory/modpacks/tensura_neo_otherworld/lang'/(ns+'.json')]:
   if path.exists():memory.update(read(path))
  for k,v in en.items():
   if k in th or not isinstance(v,str):continue
   new=None;via=None
   if ns=='foxablazeaqzl_wiki' and k.removeprefix(ns+'.') in manual:new=manual[k.removeprefix(ns+'.')];via='context-reviewed UI'
   if new is None:
    entry=memory.get(k,{})
    if isinstance(entry,dict) and entry.get('en')==v and isinstance(entry.get('th'),str) and re.search('[ก-๛]',entry['th']):new=entry['th'];via='exact-source namespace memory'
   if new is not None:
    errors,warnings=m.check_item('lang|'+ns+'|'+k,v,new,{})
    if not errors:
     new=re.sub('[§&][lo]','',new);th[k]=new;added.append({'namespace':ns,'key':k,'en':v,'th':new,'via':via});continue
   if re.search(r'advancements?\.|(^|\.)(config|settings|commands?)\.',k):excluded['advancement_config_command']+=1;continue
   if k.startswith(('item.','block.','entity.','key.','effect.')) or k.endswith('.name'):excluded['name_or_label_needs_context']+=1;continue
   if len(v)>35 and re.search('[A-Za-z]{3,} [A-Za-z]{3,}',v):pending.append({'namespace':ns,'key':k,'en':v})
  write(p,th)
 write(R/'review/ui-repair-added.json',added);write(R/'review/ui-unfiltered-pending.json',pending)
 write(R/'review/ui-scan-summary.json',{'added':len(added),'unmatched_sentence_candidates':len(pending),'excluded_not_certified':dict(excluded),'complete':not pending,'runtime_test':'NOT_RUN'})
 print('Added:',len(added),'Remaining sentence candidates:',len(pending),'Excluded requiring scope/context:',dict(excluded))
if __name__=='__main__':main()
