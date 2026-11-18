"""Pattern translation for repetitive lines: python pat.py N  -> merges ans/NNNm.json (manual) with generated lines into ans/NNN.json."""
import json, os, re, sys
W = os.path.dirname(os.path.abspath(__file__))
B = 120
RULES = [
    (r'^Dropped (%1\$s) - requires: (.*)$', r'ตัด \1 ออก - ต้องมี: \2'),
    (r'^Requires: (.*) for (\'%\d+\$s\')\.$', r'ต้องมี: \1 สำหรับ \2'),
    (r'^Requires: (.*)$', r'ต้องมี: \1'),
]
POST = [(', or ', ' หรือ '), (' or ', ' หรือ '), (' (mastered)', ' (เชี่ยวชาญแล้ว)')]


VERBS = {'Submit': 'ส่ง', 'Collect': 'เก็บ', 'Craft': 'คราฟต์', 'Subjugate': 'ปราบ', 'Find': 'หา', 'Investigate': 'สำรวจ', 'Clear': 'กวาดล้าง', 'Stop': 'หยุด', 'Kill': 'สังหาร', 'Slay': 'สังหาร', 'Mine': 'ขุด', 'Smith': 'ตีเหล็ก', 'Master': 'เชี่ยวชาญ'}


def gen(en):
    m = re.match(r'^(Submit|Collect|Craft|Subjugate|Find|Investigate|Clear|Stop|Kill|Slay|Mine|Smith|Master) (.+)$', en)
    if m and len(en) < 70 and not en.endswith('.'):
        return VERBS[m.group(1)] + ' ' + m.group(2)
    for a, b in RULES:
        if re.match(a, en):
            s = re.sub(a, b, en)
            for x, y in POST:
                s = s.replace(x, y)
            return s
    return None


if __name__ == '__main__':
    n = int(sys.argv[1])
    t = json.load(open(os.path.join(W, 'todo.json'), encoding='utf-8'))
    p = os.path.join(W, 'ans', f'{n:03d}m.json')
    out = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    for i in range((n - 1) * B, min(n * B, len(t))):
        if str(i) not in out:
            k = t[i]['keys'][0]
            if re.search(r'\.ui\.name\.|\.skill\.mode\.|\.mode\.[^.]+\.[^.]+$', k) and not t[i]['en'].endswith(('.', '!')):
                out[str(i)] = '='; continue
            g = gen(t[i]['en'])
            if g: out[str(i)] = g
    json.dump(out, open(os.path.join(W, 'ans', f'{n:03d}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('entries', len(out))
