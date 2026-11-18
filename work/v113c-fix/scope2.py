"""Scope for the fix round: every player-facing missing key except names and advancements."""
import json, sys, re, collections, os, glob
sys.stdout.reconfigure(encoding='utf-8')
O = sys.argv[1]
SK = r'D:/minecraft/modpack-thai-translator'
c = json.load(open(r'D:/minecraft/Tensura_Neo_Otherworld_Thai/work/v113c/cache/lang_sources.json', encoding='utf-8'))
SKIPNS = re.compile(r'^(minecraft|realms|fabric.*|forge|neoforge|sodium.*|iris|indium|modmenu|cloth.?config.*|yet_?another_?config.*|yacl.*|fancymenu|konkrete|drippyloadingscreen|entity_(model|texture)_features|controlling|xaero.*|journeymap|voicechat|betterf3|lambdynlights|immediatelyfast|modernfix|ferritecore|krypton|c2me.*|debugify|puzzle|continuity|polytone|resourcepackoverrides|bettermodsbutton|chat_heads|reeses-sodium-options|jupiter|melody|loadmyresources|spark|mixin.*|connectivity|embeddium.*|nochatreports|betterpingdisplay|fpsreducer|dynamic_fps|entityculling|enhancedblockentities|moreculling|threadtweak|noisium|smoothboot.*|starlight|memoryleakfix|clumps|packetfixer)$')
ADV = re.compile(r'(^|\.)advancements?\.|(^|\.)commands?\.|^death\.attack|^key\.|^stat\.|^subtitles?\.|^itemGroup\.|creative_?tab|itemgroup|^tag\.|^modmenu\.|^text\.autoconfig')
NAMEKEY = re.compile(r'^(item|block|entity|effect|enchantment|biome|painting|trim_material|trim_pattern|instrument|jukebox_song|fluid|fluid_type|attribute\.name|dimension)\.|\.name$|\.skill\.[^.]+$|\.race\.[^.]+$|\.skill\.mode\.|\.magic\.[^.]+$|\.mode\.[^.]+\.[^.]+$|^skill\.|\.wiki\.(skill|item|additional_skill)\.')
CFG = re.compile(r'(^|[._])(config|configs|configuration|options?|settings?|midnightconfig|cfg|gui\.config)([._]|$)', re.I)
DESC = re.compile(r'(desc|tooltip|lore|info|hint|message|msg|usage|help|warn|error|fail|success|explanation|flavou?r|story|text|line|subtitle|label|button|status|confirm|prompt)', re.I)

HARD = re.compile(r'^(item|block|entity|effect|enchantment|biome|painting|fluid|fluid_type|item_tab|itemGroup)\.')
def is_name(k, v):
    if DESC.search(k.split('.')[-1]): return False
    if HARD.search(k) and k.count('.') <= 3 and not v.rstrip().endswith(('.', '!', '?', '...')): return True
    if len(v.split()) > 5: return False
    if NAMEKEY.search(k): return True
    return False

# Existing Thai by English: every th_th we ship + skill memory text
by_en = collections.defaultdict(collections.Counter)
for ns, en in c['en'].items():
    p = os.path.join(O, 'translation-src/lang', ns, 'lang/th_th.json')
    if not os.path.exists(p): continue
    th = json.load(open(p, encoding='utf-8-sig'))
    for k, v in en.items():
        if k in th and isinstance(v, str) and th[k] != v: by_en[v][th[k]] += 1
for f in glob.glob(SK + '/memory/**/*.json', recursive=True):
    try: d = json.load(open(f, encoding='utf-8'))
    except Exception: continue
    if isinstance(d, dict):
        for k, e in d.items():
            if isinstance(e, dict) and isinstance(e.get('en'), str) and isinstance(e.get('th'), str) and e['th'] != e['en'] and re.search('[ก-๛]', e['th']):
                by_en[e['en']][e['th']] += 1

todo = []; auto = {}; stat = collections.Counter(); per = collections.Counter()
for ns, en in c['en'].items():
    if SKIPNS.match(ns): stat['skip_ns'] += 1; continue
    p = os.path.join(O, 'translation-src/lang', ns, 'lang/th_th.json')
    th = json.load(open(p, encoding='utf-8-sig')) if os.path.exists(p) else {}
    for k, v in en.items():
        if k in th or not isinstance(v, str) or not re.search('[A-Za-z]{2}', v): continue
        if ADV.search(k): stat['adv'] += 1; continue
        if not ns.startswith(('tensura','greatsage','tno')) and CFG.search(k): stat['cfg'] += 1; continue
        if is_name(k, v): stat['name'] += 1; continue
        if v in by_en:
            auto[ns + '|' + k] = by_en[v].most_common(1)[0][0]; stat['auto'] += 1; continue
        todo.append({'ns': ns, 'k': k, 'en': v}); per[ns] += 1; stat['todo'] += 1
print(stat); print(per.most_common(50))
print('todo chars', sum(len(x['en']) for x in todo), 'unique en', len({x['en'] for x in todo}))
json.dump({'auto': auto, 'todo': todo}, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
