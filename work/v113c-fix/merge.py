"""Merge done.json + auto.json into translation-src/lang/<ns>/lang/th_th.json (only keys that are missing).
Strips bold/italic codes like tools/fix_font_styles.py, turns a literal backslash-n into a real newline when the English has one."""
import json, os, re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
W = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(W, '..', '..'))
LANG = os.path.join(R, 'translation-src', 'lang')
todo = json.load(open(os.path.join(W, 'todo.json'), encoding='utf-8'))
done = json.load(open(os.path.join(W, 'done.json'), encoding='utf-8'))
auto = json.load(open(os.path.join(W, 'auto.json'), encoding='utf-8'))
cache = json.load(open(os.path.join(R, 'work', 'v113c', 'cache', 'lang_sources.json'), encoding='utf-8'))['en']
add = collections.defaultdict(dict)
fixnl = same = 0


def clean(en, th):
    global fixnl
    if '\n' in en and '\n' not in th and '\\n' in th:
        th = th.replace('\\n', '\n'); fixnl += 1
    return re.sub(r'[§&][lo]', '', th)


for x in todo:
    th = done.get(x['en'])
    if th is None: continue
    if th == x['en']: same += 1; continue
    th = clean(x['en'], th)
    for k in x['keys']:
        ns, key = k.split('|', 1)
        add[ns][key] = th
for k, th in auto.items():
    ns, key = k.split('|', 1)
    en = cache[ns].get(key, '')
    add[ns].setdefault(key, clean(en, th))
tot = 0
for ns, d in add.items():
    p = os.path.join(LANG, ns, 'lang', 'th_th.json')
    cur = json.load(open(p, encoding='utf-8-sig')) if os.path.exists(p) else {}
    n = 0
    for k, v in d.items():
        if k not in cur:
            cur[k] = v; n += 1
    if n:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(cur, f, ensure_ascii=False, indent=2); f.write('\n')
        tot += n
print('namespaces', len(add), 'keys added', tot, '| newline fixes', fixnl, '| kept English (not written)', same)
