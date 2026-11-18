"""Fix round (2026-11-18): missing player-facing lang keys that the first scope filtered out.

  python fx.py init <scope2.json>   -> todo.json (unique English, priority order) + auto.json
  python fx.py show N               -> print batch N (index<TAB>English)
  python fx.py apply N              -> check ans/NNN.json, store into done.json
  python fx.py stat
Answers: ans/NNN.json = {"<index>": "ไทย", ...}; "=" means keep the English.
"""
import json, sys, os, re, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
W = os.path.dirname(os.path.abspath(__file__))
B = 120
PRI = ['tensura', 'tensura_tno', 'tensuramoreskills', 'greatsage', 'tensura_guild', 'tensura_blade', 'tensurabarriers',
       'tno_tensura_extras', 'tensura_kumodesu', 'tensura_neb', 'tensura_ftb', 'tensura_trepu', 'traddon', 'mysticism',
       'foxablazeultimate', 'foxablazeaqzl_wiki', 'tennogamenolife', 'mortal_cultivation', 'stextras', 'beyond_gacha_c']


def rj(p, d=None):
    p = os.path.join(W, p)
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else d


def wj(p, x):
    with open(os.path.join(W, p), 'w', encoding='utf-8') as f:
        json.dump(x, f, ensure_ascii=False, indent=1)


def init(src):
    s = json.load(open(src, encoding='utf-8'))
    rank = lambda ns: PRI.index(ns) if ns in PRI else len(PRI)
    todo = sorted(s['todo'], key=lambda x: (rank(x['ns']), x['ns'], x['k']))
    uniq = {}
    for x in todo:
        uniq.setdefault(x['en'], []).append(x['ns'] + '|' + x['k'])
    wj('todo.json', [{'en': en, 'keys': ks} for en, ks in uniq.items()])
    wj('auto.json', s['auto'])
    print('unique', len(uniq), 'batches', (len(uniq) + B - 1) // B)


def show(n):
    t = rj('todo.json')
    for i in range((n - 1) * B, min(n * B, len(t))):
        x = t[i]
        print(f"{i}\t{x['keys'][0].split('|')[1]}\t{json.dumps(x['en'], ensure_ascii=False)}")


def mtt():
    p = os.path.join(W, '..', '..', '..', 'modpack-thai-translator', 'scripts', 'mtt.py')
    sp = importlib.util.spec_from_file_location('mtt', p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def apply(n):
    m = mtt()
    t = rj('todo.json'); done = rj('done.json', {})
    a = rj(f'ans/{n:03d}.json')
    lo, hi = (n - 1) * B, min(n * B, len(t))
    err = 0
    missing = [i for i in range(lo, hi) if str(i) not in a]
    if missing:
        print('missing', missing); err += 1
    for si, th in a.items():
        i = int(si)
        x = t[i]
        if th == '=':
            th = x['en']
        e, w = m.check_item('lang|' + x['keys'][0], x['en'], th, {})
        if x['en'][:1].isspace() != th[:1].isspace() or x['en'][-1:].isspace() != th[-1:].isspace():
            e = e + ['edge whitespace']
        if e:
            err += 1; print(i, e, '|', x['en'], '|', th)
            continue
        for w1 in w:
            if 'English' not in w1:
                print('  warn', i, w1)
        done[x['en']] = th
    wj('done.json', done)
    print('batch', n, 'errors', err, '| done', len(done), '/', len(t))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'init': init(sys.argv[2])
    elif cmd == 'show': show(int(sys.argv[2]))
    elif cmd == 'apply': apply(int(sys.argv[2]))
    elif cmd == 'stat':
        print(len(rj('done.json', {})), '/', len(rj('todo.json')))
