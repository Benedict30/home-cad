"""Check a plan before building the app: every piece of furniture inside its room (or a room it was opened up to),
clear of walls, door swings and other furniture. Pure Python, no extra packages.
Usage: python3 check_plan.py plan.json      (exit code 1 if anything needs fixing)"""
import json, math, sys

def corners(f, pad=0):
    a = math.radians(f.get('rot', 0) or 0); c, s = math.cos(a), math.sin(a); hw, hd = f['w'] / 2 + pad, f['d'] / 2 + pad
    return [(f['x'] + x * c - y * s, f['y'] + x * s + y * c) for x, y in ((-hw, -hd), (hw, -hd), (hw, hd), (-hw, hd))]
def wall_quad(a, b, t):
    L = math.dist(a, b) or 1; nx, ny = -(b[1] - a[1]) / L * t / 2, (b[0] - a[0]) / L * t / 2
    return [(a[0] + nx, a[1] + ny), (b[0] + nx, b[1] + ny), (b[0] - nx, b[1] - ny), (a[0] - nx, a[1] - ny)]
def overlap(P, Q, tol=8):   # separating axis test for convex polygons, ignoring touches under tol mm
    for poly in (P, Q):
        for i in range(len(poly)):
            x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % len(poly)]; ax, ay = y1 - y2, x2 - x1; n = math.hypot(ax, ay) or 1; ax, ay = ax / n, ay / n
            p = [x * ax + y * ay for x, y in P]; q = [x * ax + y * ay for x, y in Q]
            if max(p) <= min(q) + tol or max(q) <= min(p) + tol: return False
    return True
def inside(pt, poly):
    x, y = pt; c = False; j = len(poly) - 1
    for i in range(len(poly)):
        if (poly[i][1] > y) != (poly[j][1] > y) and x < (poly[j][0] - poly[i][0]) * (y - poly[i][1]) / (poly[j][1] - poly[i][1]) + poly[i][0]: c = not c
        j = i
    return c
def near_seg(pt, a, b, r):
    vx, vy = b[0] - a[0], b[1] - a[1]; L2 = vx * vx + vy * vy or 1; t = max(0, min(1, ((pt[0] - a[0]) * vx + (pt[1] - a[1]) * vy) / L2))
    return math.hypot(pt[0] - a[0] - t * vx, pt[1] - a[1] - t * vy) <= r

def check(plan):
    W = {w['id']: w for w in plan['walls']}; rooms = plan['rooms']; problems = []
    for L in plan['layouts']:
        removed = set(L.get('removed') or []); walls = [w for w in plan['walls'] if w['type'] != 'open' and w['id'] not in removed]
        gone = [W[i] for i in removed if i in W]
        swings = []
        for o in plan.get('openings') or []:
            if o['type'] != 'door' or o['wall'] in removed or o['wall'] not in W: continue
            w = W[o['wall']]; Lw = math.dist(w['a'], w['b']) or 1; ux, uy = (w['b'][0] - w['a'][0]) / Lw, (w['b'][1] - w['a'][1]) / Lw
            sg = -1 if o.get('flip') else 1; nx, ny = -uy * sg, ux * sg
            p0 = (w['a'][0] + ux * o['at'], w['a'][1] + uy * o['at']); p1 = (p0[0] + ux * o['w'], p0[1] + uy * o['w'])
            swings.append((o['wall'], [p0, p1, (p1[0] + nx * o['w'], p1[1] + ny * o['w']), (p0[0] + nx * o['w'], p0[1] + ny * o['w'])]))
        solid = [f for f in L['furniture'] if f.get('kind') != 'rug' and (f.get('z') or 0) < 1200]
        for f in L['furniture']:
            name = f"{L['id']}: {f['name']}"; C = corners(f, -10)
            ok_pt = lambda p: any(inside(p, r['poly']) for r in rooms) or any(near_seg(p, w['a'], w['b'], (w.get('t') or 120) / 2 + 30) for w in gone)
            if not all(ok_pt(p) for p in C + [((C[i][0] + C[(i + 1) % 4][0]) / 2, (C[i][1] + C[(i + 1) % 4][1]) / 2) for i in range(4)]):
                problems.append(name + ' sticks out of the flat')
            if f.get('kind') == 'rug': continue
            spans_gap = 'gate' in f['name'].lower()   # gates and screens sit across an opening, between walls
            for w in ([] if spans_gap else walls):
                if overlap(C, wall_quad(w['a'], w['b'], w.get('t') or 120)): problems.append(f"{name} runs into wall {w['id']}")
            for wid, sq in swings:
                if overlap(C, sq, 20): problems.append(f"{name} blocks the door on {wid}")
            if f not in solid: continue
            for g in solid:
                if g is f or id(g) < id(f): continue
                pair = {f.get('kind'), g.get('kind')}
                if 'chair' in pair and pair & {'table', 'desk'}: continue   # chairs tuck under tables and desks
                if overlap(C, corners(g, -10)): problems.append(f"{name} overlaps {g['name']}")
    return problems

if __name__ == '__main__':
    plan = json.load(open(sys.argv[1])); p = check(plan)
    print('\n'.join(p) if p else f"OK: {sum(len(L['furniture']) for L in plan['layouts'])} pieces in {len(plan['layouts'])} layouts fit")
    sys.exit(1 if p else 0)
