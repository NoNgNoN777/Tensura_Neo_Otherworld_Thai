"""Round 2 gap fix (2026-11-18): player-visible Tensura-family messages still missing from th_th.
Check with mtt, then write into translation-src th_th.json and skill memory (missing keys only)."""
import json, os, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
W = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(W, '..', '..'))
sp = importlib.util.spec_from_file_location('mtt', os.path.join(R, '..', 'modpack-thai-translator', 'scripts', 'mtt.py'))
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
cache = json.load(open(os.path.join(R, 'work', 'v113c', 'cache', 'lang_sources.json'), encoding='utf-8'))['en']
SK = os.path.join(R, '..', 'modpack-thai-translator', 'memory', 'modpacks', 'tensura_neo_otherworld', 'lang')
B = 'tensura_tno.compat.tensurabarriers.common.command.'
T = {
 # --- reported: Insanity effect + Ronova ---
 'tensura|effect.tensura.insanity.fear': 'คุณสะดุ้งตื่นด้วยความหวาดกลัว...',
 'tensura|effect.tensura.insanity.gaze': 'คุณรู้สึกถึงสายตาเย็นเยียบที่จ้องมอง...',
 'tensuramoreskills|skill.tensuramoreskills.ronova.incarnate_on': 'Death Incarnate: ซ่อนแล้ว',
 'tensuramoreskills|skill.tensuramoreskills.ronova.incarnate_off': 'Death Incarnate: เผยแล้ว',
 # --- core skill/race messages (action bar / chat) ---
 'tensura|tensura.race.cooldown': 'ความสามารถของ %s ติดคูลดาวน์',
 'tensura|tensura.skill.acquire_mode': '%s: ได้รับ %s แล้ว',
 'tensura|tensura.skill.acquire_temporary': 'ได้รับ %s ชั่วคราวแล้ว',
 'tensura|tensura.skill.already_has': '%s มี %s อยู่แล้ว',
 'tensura|tensura.skill.check_flight': '%s กำลังบินอย่างถูกต้อง',
 'tensura|tensura.skill.cooldown': '%s ติดคูลดาวน์',
 'tensura|tensura.skill.do_not_have': '%s ไม่มี %s',
 'tensura|tensura.skill.empty_storage': '%s ไม่มีความสามารถใดเลย',
 'tensura|tensura.skill.invalid': '%s ไม่ถูกต้อง',
 'tensura|tensura.skill.lack_aura': 'ออร่าหมด',
 'tensura|tensura.skill.lack_magicule': 'มาจิคูลหมด',
 'tensura|tensura.skill.no_skill': '%s ไม่มี %s',
 'tensura|tensura.skill.spatial_blockade': 'การเคลื่อนที่เชิงมิติของคุณถูกปิดกั้น',
 'tensura|tensura.skill.time_held': 'เวลาเปิดใช้: %s',
 # --- statistics screen ---
 'tensura|stat.tensura.battlewill_learnt': 'จำนวน Battlewill ที่เรียนรู้',
 'tensura|stat.tensura.battlewill_mastered': 'จำนวน Battlewill ที่เชี่ยวชาญ',
 'tensura|stat.tensura.boss_defeated': 'จำนวนบอส unique ที่เอาชนะ',
 'tensura|stat.tensura.entity_named': 'จำนวนเอนทิตีที่ตั้งชื่อให้',
 'tensura|stat.tensura.magic_learnt': 'จำนวนเวทที่เรียนรู้',
 'tensura|stat.tensura.magic_mastered': 'จำนวนเวทที่เชี่ยวชาญ',
 'tensura|stat.tensura.skill_learnt': 'จำนวนสกิลที่เรียนรู้',
 'tensura|stat.tensura.skill_mastered': 'จำนวนสกิลที่เชี่ยวชาญ',
 'tensura|stat.tensura.spirit_contracted_time': 'จำนวนครั้งที่ทำสัญญาวิญญาณสำเร็จ',
 'tensura|stat.tensura.spirit_pray_fail_time': 'จำนวนครั้งที่อธิษฐานวิญญาณล้มเหลว',
 'tensura|stat.tensura.spirit_pray_time': 'จำนวนครั้งที่อธิษฐานขอ Elemental Spirit',
 # --- controls / GUI labels ---
 'tensura|key.categories.hidden': 'ซ่อน',
 'tensura|key.number_0': 'ปุ่มตัวเลข 0',
 'tensuramoreskills|key.tensuramoreskills.ewigkeit_skip': 'ข้ามฉาก Ewigkeit',
 'tensuramoreskills|tensuramoreskills.gui.nirvana.sort.name': 'ชื่อ',
 'tensuramoreskills|tensuramoreskills.gui.gene_editor.header': 'คลังยีน',
 # --- /barrier player command messages (perf/reload/op-only left English) ---
 'tensura_tno|tensura_tno.compat.tensurabarriers.common.skill.mana': 'ต้องมีสกิล: Mana Manipulation',
 'tensura_tno|' + B + 'share.self': 'คุณเป็นเจ้าของอยู่แล้ว',
 'tensura_tno|' + B + 'share.location': 'ยืนอยู่ในบาเรียร์ที่คุณเป็นเจ้าของ (หรือระบุ id)',
 'tensura_tno|' + B + 'share.not_owned': 'คุณไม่ได้เป็นเจ้าของบาเรียร์นั้น',
 'tensura_tno|' + B + 'share.already': 'บาเรียร์นั้นแชร์อยู่แล้ว',
 'tensura_tno|' + B + 'share.owner_offline': 'เจ้าของบาเรียร์ต้องออนไลน์อยู่',
 'tensura_tno|' + B + 'share.gone': 'บาเรียร์นั้นไม่มีอยู่แล้ว',
 'tensura_tno|' + B + 'share.no_offer': 'ไม่มีข้อเสนอแชร์บาเรียร์ที่รออยู่',
 'tensura_tno|' + B + 'share.offered': 'เสนอแชร์บาเรียร์ #%1$s ให้ %2$s แล้ว (60 วินาที)',
 'tensura_tno|' + B + 'share.invitation': '%1$s เสนอแชร์บาเรียร์ %2$s ของเขา - คุณจะเป็นเจ้าของร่วมและแบ่งค่าบำรุงรักษากัน ',
 'tensura_tno|' + B + 'share.accepted': 'ตอนนี้คุณเป็นเจ้าของร่วมของบาเรียร์ #%1$s - แบ่งค่าบำรุงรักษาและใช้โบนัสร่วมกัน',
 'tensura_tno|' + B + 'share.coowner': '%1$s เป็นเจ้าของร่วมของบาเรียร์ #%2$s แล้ว',
 'tensura_tno|' + B + 'corner.player': 'เฉพาะผู้เล่นเท่านั้นที่กำหนดมุมได้',
 'tensura_tno|' + B + 'corner.already': 'คุณกำหนดมุมครบ 3 มุมแล้ว - /barrier create <type> หรือ /barrier corner clear',
 'tensura_tno|' + B + 'corner.cleared': 'ล้างมุมแล้ว',
 'tensura_tno|' + B + 'corner.marked': 'กำหนดมุม %1$s/3 ที่ %2$s/%3$s/%4$s แล้ว',
 'tensura_tno|' + B + 'corner.ready': 'กำหนดมุม %1$s/3 ที่ %2$s/%3$s/%4$s แล้ว พร้อมแล้ว - /barrier create <type>',
 'tensura_tno|' + B + 'create.failed': 'สร้างบาเรียร์ไม่ได้ (มุมผิดรูป หรือถึงขีดจำกัดต่อมิติแล้ว?)',
 'tensura_tno|' + B + 'create.unknown': "ไม่รู้จักบาเรียร์ชนิด '%1$s' ชนิดที่มี: %2$s",
 'tensura_tno|' + B + 'create.requires': 'การสร้างบาเรียร์ %1$s ต้องมีอย่างใดอย่างหนึ่ง: %2$s',
 'tensura_tno|' + B + 'create.triangle': "'%1$s' เป็นบาเรียร์สามเหลี่ยม - กำหนด 3 มุมด้วย /barrier corner ก่อน",
 'tensura_tno|' + B + 'create.panel': "'%1$s' เป็นบาเรียร์แผ่น - กำหนด 2 มุมด้วย /barrier corner (หรือใช้ /barrier panel)",
 'tensura_tno|' + B + 'panel.failed': 'สร้างแผ่นไม่ได้ (มุมอยู่ใกล้กันเกินไปบนแกนหน้าทั้งสอง?)',
 'tensura_tno|' + B + 'panel.placed': 'วางบาเรียร์แผ่น %1$s #%2$s แล้ว',
 'tensura_tno|' + B + 'panel.wrong_type': "'%1$s' ไม่ใช่บาเรียร์ชนิดแผ่น",
 'tensura_tno|' + B + 'remove.owner': 'เฉพาะเจ้าของบาเรียร์ (หรือ op) เท่านั้นที่สลายได้',
 'tensura_tno|' + B + 'remove.none': 'ไม่มีบาเรียร์ให้ลบ',
 'tensura_tno|' + B + 'remove.none_owned': 'คุณไม่ได้เป็นเจ้าของบาเรียร์ใดเลย (op ใช้ /barrier remove all ได้ทั้งโลก)',
 'tensura_tno|' + B + 'remove.missing': 'ไม่มีบาเรียร์ id %1$s',
 'tensura_tno|' + B + 'remove.owned': 'สลายบาเรียร์ของคุณแล้ว %1$s อัน',
 'tensura_tno|' + B + 'damage.indestructible': 'บาเรียร์ #%1$s ทำลายไม่ได้',
 'tensura_tno|' + B + 'list.none': 'ไม่มีบาเรียร์ที่ทำงานอยู่',
 'tensura_tno|' + B + 'zone.outside': 'คุณไม่ได้ยืนอยู่ในเขตห้ามบาเรียร์',
 'tensura_tno|' + B + 'zone.here': 'อยู่ในเขตห้ามบาเรียร์: %1$s',
 'tensura_tno|' + B + 'import.player': 'เฉพาะผู้เล่นเท่านั้นที่นำเข้าแบบบาเรียร์ได้',
 'tensura_tno|' + B + 'import.too_long': 'โค้ดแชร์นั้นยาวเกินไปมาก',
 'tensura_tno|' + B + 'created.000': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s',
 'tensura_tno|' + B + 'created.001': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s เสริมพลังโดย %5$s',
 'tensura_tno|' + B + 'created.010': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s ค่าบำรุงรักษา %5$s มาจิคูล/วิ',
 'tensura_tno|' + B + 'created.011': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s ค่าบำรุงรักษา %5$s มาจิคูล/วิ เสริมพลังโดย %6$s',
 'tensura_tno|' + B + 'created.100': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s ความทนทาน %5$s',
 'tensura_tno|' + B + 'created.101': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s ความทนทาน %5$s เสริมพลังโดย %6$s',
 'tensura_tno|' + B + 'created.111': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s ความทนทาน %5$s ค่าบำรุงรักษา %6$s มาจิคูล/วิ เสริมพลังโดย %7$s',
 'tensura_tno|' + B + 'created.110': 'สร้างบาเรียร์ %1$s #%2$s แล้ว - %3$s ขนาด %4$s ความทนทาน %5$s ค่าบำรุงรักษา %6$s มาจิคูล/วิ',
}
# created.111 has a long tail; build from English to keep every placeholder
e111 = cache['tensura_tno'].get(B + 'created.111', '')
print('created.111 EN:', repr(e111))
bad = 0; add = {}
for k, th in T.items():
    ns, key = k.split('|', 1); en = cache[ns].get(key)
    if en is None: print('NO EN', k); bad += 1; continue
    errs, warns = m.check_item('lang|' + k, en, th, {})
    if (en[:1].isspace(), en[-1:].isspace()) != (th[:1].isspace(), th[-1:].isspace()): errs = list(errs) + ['edge space']
    if errs: print('ERR', k, errs, '|', en, '|', th); bad += 1; continue
    add.setdefault(ns, {})[key] = (en, th)
print('ok', sum(map(len, add.values())), 'bad', bad)
if bad or '--write' not in sys.argv: sys.exit(0)
n = 0
for ns, d in add.items():
    p = os.path.join(R, 'translation-src', 'lang', ns, 'lang', 'th_th.json')
    cur = json.load(open(p, encoding='utf-8-sig')) if os.path.exists(p) else {}
    q = os.path.join(SK, ns + '.json'); mem = json.load(open(q, encoding='utf-8')) if os.path.exists(q) else {}
    for key, (en, th) in d.items():
        if key not in cur: cur[key] = th; n += 1
        mem[key] = {'en': en, 'th': th}
    with open(p, 'w', encoding='utf-8', newline='\n') as f: json.dump(cur, f, ensure_ascii=False, indent=2); f.write('\n')
    with open(q, 'w', encoding='utf-8') as f: json.dump(mem, f, ensure_ascii=False, indent=1)
print('written', n)
