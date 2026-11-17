import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=97
P='ponderer.ui.'
ST={'indicate_redstone':("ชี้เรดสโตน","ตัวชี้เรดสโตน"),'indicate_success':("ชี้ความสำเร็จ","ตัวชี้ความสำเร็จ"),'clear_entities':("ล้างเอนทิตี",None),'clear_item_entities':("ล้างเอนทิตีไอเทม",None),'modify_entities_nbt':("แก้ไข NBT เอนทิตี",None),'modify_item_entities_nbt':("แก้ไข NBT เอนทิตีไอเทม",None)}
EXYZ="ตำแหน่งสิ้นสุดต้องมี X, Y และ Z"
D={
'modify_block_entity_nbt.redraw.tooltip':"วาดบล็อกใหม่หลังแก้ไข",
'modify_block_entity_nbt.error.required':"จำเป็นต้องมี คุณสมบัติ หรือ NBT",
'modify_block_entity_nbt.error.invalid':"NBT ไม่ถูกต้อง",
'modify_block_entity_nbt.error.partial_to':EXYZ,
'indicate_redstone.pos':"ตำแหน่า",
'indicate_redstone.pos.tooltip':"ตำแหน่งตัวชี้ X Y Z",
'indicate_success.pos':"ตำแหน่ง",
'indicate_success.pos.tooltip':"ตำแหน่งตัวชี้ X Y Z",
'clear_entities.id':"เอนทิตี",
'clear_entities.id.hint':"เช่น minecraft:zombie (ว่าง=ทั้งหมด)",
'clear_entities.id.tooltip':"เว้นว่างเพื่อล้างทั้งหมด",
'clear_entities.pos_from.tooltip':"ตำแหน่งเริ่มต้นของการเลือก X Y Z",
'clear_entities.pos_to.tooltip':"ตำแหน่งสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'clear_entities.full_scene':"ทั้งฉาก",
'clear_entities.full_scene.tooltip':"ล้างเอนทิตีที่ตรงทั้งหมดในทั้งฉาก โดยไม่สนพิกัด",
'clear_entities.error.partial_to':EXYZ,
'clear_item_entities.id.hint':"เว้นว่างเพื่อล้างทั้งหมด",
'clear_item_entities.id.tooltip':"เว้นว่างเพื่อล้างไอเทมที่ดรอปทั้งหมด",
'clear_item_entities.pos_from.tooltip':"ตำแหน่งเริ่มต้นของการเลือก X Y Z",
'clear_item_entities.pos_to.tooltip':"ตำแหน่งสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'clear_item_entities.full_scene':"ทั้งฉาก",
'clear_item_entities.full_scene.tooltip':"ล้างไอเทมที่ดรอปที่ตรงทั้งหมดในทั้งฉาก โดยไม่สนพิกัด",
'clear_item_entities.error.partial_to':EXYZ,
'modify_entities_nbt.id':"เอนทิตี",
'modify_entities_nbt.id.hint':"เว้นว่างเพื่อจับคู่ทั้งหมด",
'modify_entities_nbt.id.tooltip':"ตัวกรอง id ประเภทเอนทิตี เว้นว่างเพื่อแก้ไขเอนทิตีที่ไม่ใช่ไอเทมทั้งหมด",
'modify_entities_nbt.pos_from.tooltip':"ตำแหน่งเริ่มต้นของการเลือก X Y Z",
'modify_entities_nbt.pos_to.tooltip':"ตำแหน่งสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'modify_entities_nbt.nbt':"NBT",
'modify_entities_nbt.nbt.tooltip':"แพตช์ Mojangson ที่รวมเข้าเอนทิตีที่ตรงแต่ละตัว",
'modify_entities_nbt.full_scene':"ทั้งฉาก",
'modify_entities_nbt.full_scene.tooltip':"แก้ไขเอนทิตีที่ตรงทั้งหมดในฉาก โดยไม่สนพิกัด",
'modify_entities_nbt.error.partial_to':EXYZ,
'modify_item_entities_nbt.id.hint':"เว้นว่างเพื่อจับคู่ทั้งหมด",
'modify_item_entities_nbt.id.tooltip':"ตัวกรอง id ไอเทมสำหรับไอเทมที่ดรอป เว้นว่างเพื่อแก้ไขไอเทมที่ดรอปทั้งหมด",
'modify_item_entities_nbt.pos_from.tooltip':"ตำแหน่งเริ่มต้นของการเลือก X Y Z",
'modify_item_entities_nbt.pos_to.tooltip':"ตำแหน่งสิ้นสุดของการเลือก X Y Z (ไม่บังคับ)",
'modify_item_entities_nbt.nbt':"NBT",
'modify_item_entities_nbt.nbt.tooltip':"แพตช์ Mojangson ที่รวมเข้าเอนทิตีไอเทมที่ดรอปที่ตรงแต่ละตัว",
'modify_item_entities_nbt.full_scene':"ทั้งฉาก",
'modify_item_entities_nbt.full_scene.tooltip':"แก้ไขไอเทมที่ดรอปที่ตรงทั้งหมดในฉาก โดยไม่สนพิกัด",
'modify_item_entities_nbt.error.partial_to':EXYZ,
'nbt_pick.tooltip':"จับคุณสมบัติและ NBT จากโลก",
'nbt_pick.middle_prompt':"ใช้ปุ่มกลางของเมาส์เพื่อเลือกไอเทม",
'nbt_pick.filled':"เติมคุณสมบัติและ NBT จาก %s แล้ว",
'block_pick.tooltip':"จับ ID บล็อก คุณสมบัติ และ NBT จากโลก",
'held_item.tooltip':"เติมจากไอเทมที่ถือ (อ่าน ID และ NBT ของไอเทมในมือหลัก)",
'held_item.error.empty':"มือหลักว่าง โปรดถือไอเทมก่อน",
}
C={
'ponderer.cmd.scene_not_found':"Ponderer: ไม่พบฉาก: %s",
'ponderer.cmd.pull.requesting':"Ponderer: กำลังร้องขอการซิงก์จากเซิร์ฟเวอร์ (โหมด: %s)...",
'ponderer.cmd.pull.no_permission':"Ponderer: ไม่มีสิทธิ์ดึงจากเซิร์ฟเวอร์",
'ponderer.cmd.pull.done':"Ponderer: ซิงก์เสร็จสิ้น (เขียน %s, ข้าม %s, ขัดแย้ง %s)",
'ponderer.cmd.pull.conflict_both':"  ขัดแย้ง: %s (ทั้งในเครื่องและเซิร์ฟเวอร์ถูกแก้ไข)",
'ponderer.cmd.pull.conflict_server':"  ขัดแย้ง: %s (เซิร์ฟเวอร์ชนะ)",
'ponderer.cmd.pull.hint_force':"  ใช้ /ponderer pull force เพื่อทับของในเครื่องด้วยเวอร์ชันเซิร์ฟเวอร์",
'ponderer.cmd.pull.hint_keep':"  ใช้ /ponderer pull keep_local เพื่อคงการเปลี่ยนแปลงในเครื่อง",
'ponderer.cmd.pull.write_failed':"  เขียนล้มเหลว: %s",
'ponderer.cmd.pull.server_skip_too_large':"Ponderer: ข้าม %s ระหว่างซิงก์เพราะใหญ่เกินไป (%s ไบต์)",
'ponderer.cmd.pull.server_skip_failed':"Ponderer: ข้าม %s ระหว่างซิงก์เพราะเซิร์ฟเวอร์อ่านไม่ได้",
'ponderer.cmd.reload.done':"Ponderer: โหลดสคริปต์ในเครื่องใหม่แล้ว (%s)",
'ponderer.cmd.download.requesting':"Ponderer: กำลังร้องขอนำเข้าสิ่งก่อสร้าง %s ...",
'ponderer.cmd.push.uploading':"Ponderer: กำลังอัปโหลดฉาก %s (โหมด: %s) ...",
'ponderer.cmd.push.structure_not_found':"Ponderer: ไม่พบแหล่งสิ่งก่อสร้างสำหรับ %s",
'ponderer.cmd.push.copy_failed':"Ponderer: คัดลอกสิ่งก่อสร้าง %s -> %s ล้มเหลว",
'ponderer.cmd.push.no_scenes':"Ponderer: ไม่มีฉากให้ผลัก",
'ponderer.cmd.push.done':"Ponderer: ผลัก %s ฉากแล้ว (โหมด: %s)",
'ponderer.cmd.push.conflict':"Ponderer: ผลักขัดแย้งสำหรับ %s - ใช้ /ponderer push force เพื่อทับเซิร์ฟเวอร์",
'ponderer.cmd.new.no_item':"Ponderer: ไม่มีไอเทมในมือหลัก",
'ponderer.cmd.new.no_nbt':"Ponderer: ไอเทมที่ถือไม่มี NBT/คอมโพเนนต์กำหนดเอง",
'ponderer.cmd.new.created':"Ponderer: สร้างฉากใหม่ %s สำหรับ %s แล้ว",
'ponderer.cmd.new.failed':"Ponderer: สร้างฉากสำหรับ %s ล้มเหลว",
'ponderer.cmd.copy.done':"Ponderer: คัดลอก %s -> %s แล้ว (ไอเทม: %s)",
'ponderer.cmd.copy.failed':"Ponderer: คัดลอกฉากล้มเหลว",
'ponderer.cmd.delete.done':"Ponderer: ลบฉาก %s แล้ว",
'ponderer.cmd.delete.failed':"Ponderer: ลบฉาก %s ล้มเหลว",
'ponderer.cmd.delete.no_scenes':"Ponderer: ไม่พบฉากสำหรับไอเทม %s",
'ponderer.cmd.delete.item_done':"Ponderer: ลบ %s ฉากสำหรับไอเทม %s แล้ว",
'ponderer.cmd.convert.to_done':"Ponderer: แปลงเป็นบริดจ์ PonderJS แล้ว -> %s",
'ponderer.cmd.convert.to_failed':"Ponderer: แปลงเป็น PonderJS ล้มเหลว: %s",
'ponderer.cmd.convert.to_all_done':"Ponderer: แปลง %s ฉากเป็นบริดจ์ PonderJS แล้ว",
'ponderer.cmd.convert.dir_not_found':"Ponderer: ไม่พบ kubejs/client_scripts/ponder/",
'ponderer.cmd.convert.scan_failed':"Ponderer: สแกน kubejs/client_scripts/ponder/ ล้มเหลว",
'ponderer.cmd.convert.from_done':"Ponderer: นำเข้า %s ฉากจาก PonderJS สำหรับ %s แล้ว",
'ponderer.cmd.convert.from_all_done':"Ponderer: นำเข้า %s ฉากจาก PonderJS แล้ว",
'ponderer.cmd.push.no_permission':"Ponderer: ไม่มีสิทธิ์อัปโหลด",
'ponderer.cmd.push.server_conflict':"Ponderer: ขัดแย้ง - เวอร์ชันเซิร์ฟเวอร์ของ %s ถูกแก้ไข ใช้ /ponderer push force เพื่อทับ หรือ /ponderer pull เพื่อรับเวอร์ชันเซิร์ฟเวอร์",
'ponderer.cmd.push.upload_ok':"Ponderer: อัปโหลดเสร็จสิ้น: %s",
'ponderer.cmd.push.upload_failed':"Ponderer: อัปโหลดล้มเหลว: %s",
'ponderer.cmd.download.no_permission':"Ponderer: ไม่มีสิทธิ์ดาวน์โหลด/นำเข้าสิ่งก่อสร้าง",
'ponderer.cmd.download.invalid_id':"Ponderer: id สิ่งก่อสร้างไม่ถูกต้อง: %s",
}
D['indicate_redstone.pos']="ตำแหน่ง"
keys=[]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    keys.append(k)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    if a in C: out[k]=C[a]; continue
    r=a[len(P):] if a.startswith(P) else a
    if r in D: out[k]=D[r]; continue
    m=re.fullmatch(r'(?:step\.type\.)?(\w+?)(?:\.(add|edit|pos_from|pos_to))?',r)
    if m and m.group(1) in ST:
        nm,ind=ST[m.group(1)]
        s=m.group(2)
        if s is None: out[k]=nm
        elif s=='add': out[k]="เพิ่ม"+(ind or nm)
        elif s=='edit': out[k]="แก้ไข"+(ind or nm) if not nm.startswith('แก้ไข') else "แก้ไข"+nm.replace('แก้ไข ','') if False else "แก้ไข"+(ind or nm)
        elif s=='pos_from': out[k]="จาก"
        elif s=='pos_to': out[k]="ถึง"
print('keys',len(keys),'out',len(out),[k.split('wiki.')[-1] for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
