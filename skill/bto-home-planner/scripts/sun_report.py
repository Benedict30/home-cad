"""Which rooms get direct sun, from which direction and when, for a plan with "north" set (see fit_unit.py).
Usage: python3 sun_report.py plan.json
Uses the same rules as the Sun study panel in the app: Singapore (1.35 N), three seasons, sun 4-60 degrees up
(higher sun is blocked by the floor above), and only windows. Prints a markdown table to put in the reply."""
import json, math, sys

SEASONS = [('Nov–Feb', -20), ('Mar–Apr, Sep–Oct', 0), ('May–Aug', 20)]
DIRS = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']


def sun(t, dec):
    d, phi, H = math.radians(dec), math.radians(1.35), math.radians((t - 13.1) * 15)   # solar noon about 1:05 pm
    E = -math.cos(d) * math.sin(H); N = math.cos(phi) * math.sin(d) - math.sin(phi) * math.cos(d) * math.cos(H)
    U = math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.cos(H)
    return math.degrees(math.asin(U)), math.degrees(math.atan2(E, N)) % 360


def inpoly(x, y, poly):
    c = False; j = len(poly) - 1
    for i in range(len(poly)):
        (xi, yi), (xj, yj) = poly[i], poly[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-9) + xi: c = not c
        j = i
    return c


def area(p): return abs(sum(p[i][0] * p[i - 1][1] - p[i - 1][0] * p[i][1] for i in range(len(p)))) / 2


def room_at(x, y, rooms):
    hits = [r for r in rooms if inpoly(x, y, r['poly'])]
    return min(hits, key=lambda r: area(r['poly'])) if hits else None


def hm(t):
    h = int(t); m = int(round((t - h) * 60))
    return f"{(h + 11) % 12 + 1}{':%02d' % m if m else ''}{'am' if h < 12 else 'pm'}"


def windows(plan):
    """(room name, outward bearing in degrees) for every window between a room and the outside."""
    th = math.radians(plan['north']); walls = {w['id']: w for w in plan['walls']}; out = []
    for o in plan.get('openings', []):
        if o.get('type') != 'window' or o.get('wall') not in walls: continue
        w = walls[o['wall']]; (ax, ay), (bx, by) = w['a'], w['b']; L = math.hypot(bx - ax, by - ay) or 1
        ux, uy = (bx - ax) / L, (by - ay) / L; nx, ny = -uy, ux; s = o['at'] + o['w'] / 2; off = (w.get('t') or 120) / 2 + 250
        mx, my = ax + ux * s, ay + uy * s; inside = outward = None
        for sg in (1, -1):
            r = room_at(mx + nx * sg * off, my + ny * sg * off, plan['rooms'])
            if r is None or 'ledge' in r['name'].lower(): outward = sg
            else: inside = r
        if inside is None or outward is None: continue
        vx, vy = nx * outward, ny * outward                                   # outward normal, plan coords (y down)
        N = vx * math.sin(th) - vy * math.cos(th); E = vx * math.cos(th) + vy * math.sin(th)
        out.append((inside['name'], math.degrees(math.atan2(E, N)) % 360))
    return out


def report(plan):
    win = windows(plan); names = list(dict.fromkeys(n for n, _ in win)); rows = {n: [] for n in names}; summary = []
    for label, dec in SEASONS:
        am, pm = {}, {}
        t = 7.0
        while t <= 19.5:
            if not 12 < t < 13:
                alt, az = sun(t, dec)
                if 4 <= alt <= 60:
                    c = math.cos(math.radians(alt))
                    for n, b in win:
                        if c * math.cos(math.radians(az - b)) >= .3:
                            d = am if t <= 12 else pm; d.setdefault(n, [t, t]); d[n][1] = t
            t += .25
        for n in names:
            cell = []
            if n in am: cell.append(f'morning to {hm(am[n][1] + .25)}')
            if n in pm: cell.append(f'**afternoon from {hm(pm[n][0])}**')
            rows[n].append(', '.join(cell) or 'no direct sun')
        pdir = DIRS[round(sun(16, dec)[1] / 22.5) % 16]
        summary.append(f"- **{label}:** afternoon sun from the {pdir} reaches "
                       + (', '.join(f'{n} ({hm(v[0])})' for n, v in sorted(pm.items(), key=lambda kv: kv[1][0])) or 'none of the windows'))
    face = {n: ', '.join(sorted({DIRS[round(b / 22.5) % 16] for m, b in win if m == n})) for n in names}
    lines = ['| Room | Windows face | ' + ' | '.join(l for l, _ in SEASONS) + ' |', '|---|---|' + '---|' * len(SEASONS)]
    lines += [f'| {n} | {face[n]} | ' + ' | '.join(rows[n]) + ' |' for n in names]
    return '\n'.join(lines) + '\n\n' + '\n'.join(summary)


if __name__ == '__main__':
    plan = json.load(open(sys.argv[1]))
    if plan.get('north') is None: print('Set "north" first: run scripts/fit_unit.py with --pick N --out plan.json'); sys.exit(1)
    print(report(plan))
