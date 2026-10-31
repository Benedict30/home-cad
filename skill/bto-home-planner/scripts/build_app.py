"""Turn the plan JSON into the CAD app file: copies assets/home-cad.html and puts the plan between the markers.
Usage: python3 build_app.py plan.json [output.html]
Without an output path it writes to /mnt/user-data/outputs/ when that folder exists (claude.ai shares files from there), else here."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TEMPLATE = os.path.join(HERE, '..', 'assets', 'home-cad.html')
TYPES = {'structural', 'shelter', 'bathroom', 'external', 'partition', 'open'}
def validate(p):
    err = []
    for k in ('walls', 'openings', 'rooms', 'layouts'):
        if not isinstance(p.get(k), list): err.append(f'missing list: {k}')
    if err: return err
    ids = [w.get('id') for w in p['walls']]
    if len(ids) != len(set(ids)): err.append('wall ids repeat')
    for w in p['walls']:
        if w.get('type') not in TYPES: err.append(f"wall {w.get('id')}: type must be one of {sorted(TYPES)}")
        if not (isinstance(w.get('a'), list) and isinstance(w.get('b'), list)): err.append(f"wall {w.get('id')}: a and b must be [x, y]")
    for o in p['openings']:
        if o.get('wall') not in ids: err.append(f"opening on unknown wall {o.get('wall')}")
    for r in p['rooms']:
        if len(r.get('poly') or []) < 3: err.append(f"room {r.get('id')}: poly needs 3+ points")
    if not p['layouts']: err.append('no layouts')
    for L in p['layouts']:
        for k in ('id', 'title', 'furniture'):
            if k not in L: err.append(f"layout {L.get('id')}: missing {k}")
        for f in L.get('furniture', []):
            if not all(isinstance(f.get(k), (int, float)) for k in ('x', 'y', 'w', 'd')): err.append(f"layout {L.get('id')}: {f.get('name')} needs numbers for x, y, w, d")
        for wid in L.get('removed', []):
            if wid not in ids: err.append(f"layout {L.get('id')}: removes unknown wall {wid}")
    return err
if __name__ == '__main__':
    plan = json.load(open(sys.argv[1])); err = validate(plan)
    if err: print('Fix the plan first:\n- ' + '\n- '.join(err)); sys.exit(1)
    html = open(TEMPLATE, encoding='utf-8').read(); marker = '/*PLAN-START*/null/*PLAN-END*/'
    if marker not in html: print('Template markers not found: copy assets/home-cad.html again'); sys.exit(1)
    data = json.dumps(plan, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join('/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data/outputs') else '.', re.sub(r'[^a-z0-9]+', '-', (plan.get('title') or 'my-flat').lower()).strip('-')[:60] + '.html')
    open(out, 'w', encoding='utf-8').write(html.replace(marker, '/*PLAN-START*/' + data + '/*PLAN-END*/', 1))
    print(f"Wrote {out} ({os.path.getsize(out) // 1024} KB): {len(plan['layouts'])} layouts. Share this file; it opens in any browser and works offline.")
