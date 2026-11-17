import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=96
P='ponderer.ui.'
ST={'encapsulate_bounds':"ห่อหุ้มขอบเขต",'set_block':"ตั้งบล็อก",'destroy_block':"ทำลายบล็อก",'replace_blocks':"แทนที่บล็อก",'hide_section':"ซ่อนส่วน",'show_section_and_merge':"แสดงส่วนและรวม",'toggle_redstone_power':"สลับพลังงานเรดสโตน",'rotate_section':"หมุนส่วน",'move_section':"ย้ายส่วน",'modify_block_entity_nbt':"แก้ไขบล็อก"}
PXYZ="ตำแหน่งเริ่มต้นต้องมี X, Y และ Z"
EXYZ="ตำแหน่งสิ้นสุดต้องมี X, Y และ Z"
D={
'play_sound.source.neutral':"เป็นกลาง",'play_sound.source.ambient':"บรรยากาศ",'play_sound.source.voice':"เสียงพูด",
'play_sound.error.required':"จำเป็นต้องมี ID เสียง",
'encapsulate_bounds':ST['encapsulate_bounds'],
'encapsulate_bounds.bounds':"ขอบเขต",
'encapsulate_bounds.bounds.tooltip':"ขนาดกล่องขอบเขต X Y Z สำหรับกล้องฉาก",
'set_block.hint':"เช่น minecraft:stone",
'set_block.tooltip':"ID บล็อกที่จะวาง เช่น minecraft:diamond_block",
'set_block.pos_from.tooltip':"ตำแหน่งเริ่มต้น X Y Z (จำนวนเต็ม)",
'set_block.pos_to.tooltip':"ตำแหน่งสิ้นสุด X Y Z สำหรับการเติม (ไม่บังคับ)",
'set_block.nbt':"NBT",
'set_block.nbt.tooltip':"แพตช์ NBT ของ block entity ที่ไม่บังคับ ใช้ทันทีหลังวาง",
'set_block.entrance_mode':"โหมดเข้า",
'set_block.entrance_mode.tooltip':"ควบคุมวิธีแสดงบล็อกที่วาง: hidden / immediate / animated",
'set_block.entrance_mode.option.hidden':"ซ่อน",
'set_block.entrance_mode.option.immediate':"ทันที",
'set_block.entrance_mode.option.animated':"มีแอนิเมชัน",
'set_block.particles':"อนุภาค",
'set_block.particles.tooltip':"แสดงอนุภาคการทำลายบล็อกเมื่อวาง",
'set_block.immediate_display':"แสดงทันที",
'set_block.immediate_display.tooltip':"หากเปิด บล็อกที่เพิ่งวางจะถูกบังคับเข้าส่วนที่กำลังเรนเดอร์ทันที",
'set_block.entrance_animation':"แอนิเมชันเข้า",
'set_block.entrance_animation.tooltip':"ทำแอนิเมชันการวางบล็อกทีละแถวในทิศทางโดยรวมที่เลือก",
'set_block.error.required':"จำเป็นต้องมี ID บล็อก",
'set_block.error.invalid_id':"ID บล็อกไม่ถูกต้อง",
'set_block.error.unknown':"ไม่รู้จักบล็อก: %s",
'set_block.error.partial_to':"ตำแหน่งสิ้นสุดของการเติมต้องมี X, Y และ Z",
'destroy_block.pos':"ตำแหน่ง",
'destroy_block.pos.tooltip':"ตำแหน่งบล็อกเป้าหมาย X Y Z",
'destroy_block.particles':"อนุภาค",
'destroy_block.particles.tooltip':"แสดงอนุภาคการทำลายเมื่อทำลาย",
'replace_blocks.hint':"เช่น minecraft:stone",
'replace_blocks.tooltip':"ID บล็อกที่ใช้แทนที่บล็อกที่ไม่ใช่อากาศที่มีอยู่",
'replace_blocks.pos_from.tooltip':"ตำแหน่งเริ่มต้น X Y Z (จำนวนเต็ม)",
'replace_blocks.pos_to.tooltip':"ตำแหน่งสิ้นสุด X Y Z สำหรับพื้นที่ (ไม่บังคับ)",
'replace_blocks.particles':"อนุภาค",
'replace_blocks.particles.tooltip':"แสดงอนุภาคการทำลายบล็อกขณะแทนที่",
'replace_blocks.error.required':"จำเป็นต้องมี ID บล็อก",
'replace_blocks.error.invalid_id':"ID บล็อกไม่ถูกต้อง",
'replace_blocks.error.unknown':"ไม่รู้จักบล็อก: %s",
'replace_blocks.error.partial_to':"ตำแหน่งสิ้นสุดของการแทนที่ต้องมี X, Y และ Z",
'hide_section.pos_from.tooltip':"จุดเริ่มต้นของการเลือก X Y Z",
'hide_section.pos_to.tooltip':"จุดสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'hide_section.direction':"ทิศทาง",
'hide_section.direction.tooltip':"ทิศทางการจาง: down/up/north/south/west/east",
'hide_section.error.partial_to':EXYZ,
'show_section_and_merge.add':"เพิ่ม แสดงส่วนและรวม",
'show_section_and_merge.edit':"แก้ไข แสดงส่วนและรวม",
'show_section_and_merge.pos_from.tooltip':"จุดเริ่มต้นของการเลือก X Y Z",
'show_section_and_merge.pos_to.tooltip':"จุดสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'show_section_and_merge.direction':"ทิศทาง",
'show_section_and_merge.direction.tooltip':"ทิศทางการจาง: down/up/north/south/west/east",
'show_section_and_merge.link.tooltip':"id ลิงก์ส่วน id เดียวกันหมายถึงทำงานบนสายส่วนอิสระเดียวกัน",
'show_section_and_merge.error.partial_to':EXYZ,
'toggle_redstone_power.add':"เพิ่ม สลับเรดสโตน",
'toggle_redstone_power.edit':"แก้ไข สลับเรดสโตน",
'toggle_redstone_power.pos_from.tooltip':"จุดเริ่มต้นของการเลือก X Y Z",
'toggle_redstone_power.pos_to.tooltip':"จุดสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'toggle_redstone_power.error.partial_to':EXYZ,
'rotate_section.link.tooltip':"id ลิงก์ส่วนเป้าหมาย เว้นว่างเพื่อสร้างอัตโนมัติจากการเลือกด้านล่าง",
'rotate_section.pos_from.tooltip':"ไม่บังคับ: จุดเริ่มต้นของการเลือก X Y Z ที่ใช้สร้างส่วนอัตโนมัติ",
'rotate_section.pos_to.tooltip':"ไม่บังคับ: จุดสิ้นสุดของการเลือก X Y Z สำหรับส่วนที่สร้างอัตโนมัติ",
'rotate_section.xyz':"หมุน XYZ",
'rotate_section.xyz.tooltip':"การหมุนเป็นองศารอบ X/Y/Z",
'rotate_section.error.partial_from':PXYZ,
'rotate_section.error.partial_to':EXYZ,
'move_section.link.tooltip':"id ลิงก์ส่วนเป้าหมาย เว้นว่างเพื่อสร้างอัตโนมัติจากการเลือกด้านล่าง",
'move_section.pos_from.tooltip':"ไม่บังคับ: จุดเริ่มต้นของการเลือก X Y Z ที่ใช้สร้างส่วนอัตโนมัติ",
'move_section.pos_to.tooltip':"ไม่บังคับ: จุดสิ้นสุดของการเลือก X Y Z สำหรับส่วนที่สร้างอัตโนมัติ",
'move_section.xyz':"ระยะเลื่อน XYZ",
'move_section.xyz.tooltip':"ระยะเลื่อน X/Y/Z",
'move_section.error.partial_from':PXYZ,
'move_section.error.partial_to':EXYZ,
'modify_block_entity_nbt.pos_from.tooltip':"จุดเริ่มต้นของการเลือก X Y Z",
'modify_block_entity_nbt.pos_to.tooltip':"จุดสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'modify_block_entity_nbt.properties':"คุณสมบัติ",
'modify_block_entity_nbt.properties.tooltip':"คุณสมบัติ block state ที่จะแก้ไข (key=value)",
'modify_block_entity_nbt.nbt':"NBT",
'modify_block_entity_nbt.nbt.tooltip':"compound tag แบบ Mojangson เช่น {CustomName:'\"Demo\"'}",
'modify_block_entity_nbt.redraw':"วาดใหม่",
}
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    r=a[len(P):] if a.startswith(P) else a
    if r in D: out[k]=D[r]; continue
    m=re.fullmatch(r'(\w+)(?:\.(add|edit|pos_from|pos_to))',r)
    if m and m.group(1) in ST:
        t=ST[m.group(1)]
        out[k]={'add':f"เพิ่ม{t}",'edit':f"แก้ไข{t}",'pos_from':"จาก",'pos_to':"ถึง"}[m.group(2)]; continue
    if r in ST: out[k]=ST[r]
print('keys',len(keys),'out',len(out),[k.split('wiki.')[-1] for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
