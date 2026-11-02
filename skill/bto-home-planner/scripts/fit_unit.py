"""Work out which way the flat faces by lining up its outline with the unit on the HDB site plan.

Usage:
  python3 fit_unit.py plan.json siteplan.png --at X Y --scale PX_PER_M [--arrow DEG]
  python3 fit_unit.py plan.json siteplan.png --at X Y --scale PX_PER_M [--arrow DEG] --pick N --out plan.json

--at     pixel position of the unit's number on the site plan (roughly the middle of the unit)
--scale  site-plan pixels per metre, from its scale bar (ticks 0 and 100 m that are 400 px apart give 4)
--arrow  direction the site plan's north arrow points, degrees clockwise from straight up (default 0)

The first form prints the best fits and writes fit_1.png, fit_2.png, ... in the current folder. Look at each one:
the right fit has the outline sitting on the unit, the main door (red dot) at the corridor or lift lobby, and the
windows (blue dots) facing outside, not into a neighbouring unit. The second form saves fit N into plan.json:
it sets "north" and, if the unit is the mirror image of the brochure plan, mirrors the plan to match the real unit.
"""
import argparse, copy, json, math, os, sys
import numpy as np
from PIL import Image, ImageDraw


def footprint(plan):
    """Room outlines plus wall strips, in mm."""
    polys = [r['poly'] for r in plan['rooms']]
    for w in plan['walls']:
        if w.get('type') == 'open': continue
        (ax, ay), (bx, by) = w['a'], w['b']; L = math.hypot(bx - ax, by - ay) or 1; t = (w.get('t') or 120) / 2
        nx, ny = -(by - ay) / L * t, (bx - ax) / L * t
        polys.append([[ax + nx, ay + ny], [bx + nx, by + ny], [bx - nx, by - ny], [ax - nx, ay - ny]])
    return polys


def markers(plan):
    """Main door(s) and window midpoints, in mm."""
    walls = {w['id']: w for w in plan['walls']}; door, win = [], []
    for o in plan.get('openings', []):
        w = walls.get(o.get('wall'))
        if not w: continue
        (ax, ay), (bx, by) = w['a'], w['b']; L = math.hypot(bx - ax, by - ay) or 1; s = (o['at'] + o['w'] / 2) / L
        pt = [ax + (bx - ax) * s, ay + (by - ay) * s]
        if o.get('type') == 'window': win.append(pt)
        elif o.get('type') == 'door' and w.get('type') == 'external': door.append(pt)
    return door, win


def transform(pts, c0, rot, mirror, k, at):
    """mm -> site-plan pixels: centre on c0, mirror x, rotate clockwise by rot (screen y is down), scale, move to at."""
    cr, sr = math.cos(math.radians(rot)), math.sin(math.radians(rot)); out = []
    for x, y in pts:
        x, y = (x - c0[0]) * k, (y - c0[1]) * k
        if mirror: x = -x
        out.append((at[0] + x * cr - y * sr, at[1] + x * sr + y * cr))
    return out


def raster(polys, size):
    im = Image.new('L', size, 0); d = ImageDraw.Draw(im)
    for p in polys: d.polygon([tuple(q) for q in p], fill=1)
    return np.asarray(im, dtype=np.float32)


def unit_colour(img, at, scale):
    """Median colour around the unit number, skipping the dark digits and white paper."""
    a = np.asarray(img).astype(np.int32); H, W = a.shape[:2]; r0, r1 = int(scale * 1.2), int(scale * 3.2)
    ys, xs = np.mgrid[max(0, at[1] - r1):min(H, at[1] + r1), max(0, at[0] - r1):min(W, at[0] + r1)]
    d = np.hypot(xs - at[0], ys - at[1]); px = a[ys, xs][(d >= r0) & (d <= r1)]
    s = px.sum(1); px = px[(s > 250) & (s < 735)]
    if len(px) < 10: px = a[ys, xs].reshape(-1, 3)
    return np.median(px, axis=0)


def corr_best(colour, fp, cx, cy, win):
    """Best shift of the footprint mask fp (centred at cx, cy) within +-win px, scored (inside - outside) / area."""
    h, w = fp.shape; y0, x0 = cy - h // 2 - win, cx - w // 2 - win
    if y0 < 0 or x0 < 0: return (-9, 0, 0)
    rg = colour[y0:y0 + h + 2 * win, x0:x0 + w + 2 * win]
    if rg.shape != (h + 2 * win, w + 2 * win): return (-9, 0, 0)
    c = np.fft.irfft2(np.fft.rfft2(rg) * np.conj(np.fft.rfft2(fp, s=rg.shape)), s=rg.shape)[:2 * win + 1, :2 * win + 1]
    area = fp.sum() or 1; sc = (2 * c - area) / area; iy, ix = np.unravel_index(int(np.argmax(sc)), sc.shape)
    return (float(sc[iy, ix]), int(ix - win), int(iy - win))


def fit(plan, img, at, scale):
    polys = footprint(plan); allp = [q for p in polys for q in p]
    xs, ys = [p[0] for p in allp], [p[1] for p in allp]; c0 = ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)
    R = math.hypot(max(xs) - min(xs), max(ys) - min(ys)) / 2000          # half-diagonal in metres
    up = max(1, math.ceil(8 / scale))                                    # work at about 8 px per metre or finer
    half = int((R + 6) * scale); box = (at[0] - half, at[1] - half, at[0] + half, at[1] + half)
    crop = img.crop(box).resize((2 * half * up, 2 * half * up), Image.NEAREST); k = scale * up / 1000
    col = unit_colour(img, at, scale); a = np.asarray(crop).astype(np.float32)
    colour = (np.linalg.norm(a - col, axis=2) < 48).astype(np.float32); cx = cy = half * up
    S = int(2 * R * 1000 * k) + 6; win = int(3 * scale * up)              # search 3 m around the unit number
    res = []
    for mirror in (False, True):
        for rot in range(0, 360, 3):
            fp = raster([transform(p, c0, rot, mirror, k, (S / 2, S / 2)) for p in polys], (S, S))
            sc, dx, dy = corr_best(colour, fp, cx, cy, win); res.append((sc, rot, mirror, dx, dy))
    res.sort(reverse=True); picks = []
    for r in res:
        if all(r[2] != p[2] or min(abs(r[1] - p[1]), 360 - abs(r[1] - p[1])) > 30 for p in picks): picks.append(r)
        if len(picks) == 3: break
    out = []
    for sc, rot, mirror, dx, dy in picks:                                  # refine: half-degree steps, small shifts
        best = (sc, rot, dx, dy)
        for r2 in np.arange(rot - 3, rot + 3.01, .5):
            fp = raster([transform(p, c0, r2, mirror, k, (S / 2, S / 2)) for p in polys], (S, S))
            s2, ddx, ddy = corr_best(colour, fp, cx + dx, cy + dy, max(2, up * 2))
            if s2 > best[0]: best = (s2, float(r2), dx + ddx, dy + ddy)
        out.append(dict(score=round(best[0], 3), rot=best[1] % 360, mirror=mirror, at=(at[0] + best[2] / up, at[1] + best[3] / up)))
    return out, c0, crop, box, up, k, polys


def plan_north(rot, arrow):
    """North in the (possibly mirrored) plan: degrees clockwise from the plan's up direction."""
    sx, sy = math.sin(math.radians(arrow)), -math.cos(math.radians(arrow))       # north on the site plan (y down)
    c, s = math.cos(math.radians(-rot)), math.sin(math.radians(-rot))            # undo the rotation
    px, py = sx * c - sy * s, sx * s + sy * c
    return round(math.degrees(math.atan2(px, -py)) % 360, 1)


def mirror_plan(p):
    xs = [c for w in p['walls'] for c in (w['a'][0], w['b'][0])]; X = min(xs) + max(xs); f = lambda q: [X - q[0], q[1]]
    q = copy.deepcopy(p)
    for w in q['walls']: w['a'], w['b'] = f(w['a']), f(w['b'])
    for o in q.get('openings', []):
        if o.get('type') == 'door': o['flip'] = not o.get('flip', False)    # same hinge end, swing side flips
    for r in q['rooms']:
        r['poly'] = [f(pt) for pt in r['poly']][::-1]
        if r.get('label'): r['label'] = f(r['label'])
    for L in q.get('layouts', []):
        for a in L.get('added', []): a['a'], a['b'] = f(a['a']), f(a['b'])
        for it in L.get('furniture', []): it['x'] = X - it['x']; it['rot'] = (-(it.get('rot') or 0)) % 360
    if q.get('start'): q['start'] = f(q['start'])
    if 'startYaw' in q: q['startYaw'] = (180 - q['startYaw']) % 360
    q['mirrored'] = not p.get('mirrored', False)
    return q


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('plan'); ap.add_argument('site')
    ap.add_argument('--at', nargs=2, type=float, required=True); ap.add_argument('--scale', type=float, required=True)
    ap.add_argument('--arrow', type=float, default=0); ap.add_argument('--pick', type=int); ap.add_argument('--out')
    a = ap.parse_args(); plan = json.load(open(a.plan)); img = Image.open(a.site).convert('RGB'); at = (int(a.at[0]), int(a.at[1]))
    fits, c0, crop, box, up, k, polys = fit(plan, img, at, a.scale); door, win = markers(plan)
    if a.pick:
        f = fits[a.pick - 1]; q = mirror_plan(plan) if f['mirror'] else copy.deepcopy(plan); q['north'] = plan_north(f['rot'], a.arrow)
        json.dump(q, open(a.out or a.plan, 'w'), ensure_ascii=False, indent=1)
        print(f"Saved fit {a.pick} to {a.out or a.plan}: north = {q['north']} degrees clockwise from the plan's up"
              + (", plan mirrored to match the unit (it is the mirror image of the brochure plan)" if f['mirror'] else '') + '.')
        return
    folder = os.getcwd()
    view = img.crop(box).resize(crop.size, Image.BICUBIC)
    print(f"Unit colour sampled near ({at[0]}, {at[1]}). Best fits (scores are only a rough ranking; decide by looking at the images):")
    for i, f in enumerate(fits, 1):
        im = view.copy().convert('RGB'); d = ImageDraw.Draw(im); loc = ((f['at'][0] - box[0]) * up, (f['at'][1] - box[1]) * up)
        for p in polys[:len(plan['rooms'])]:
            pts = transform(p, c0, f['rot'], f['mirror'], k, loc); d.line(pts + [pts[0]], fill=(220, 30, 30), width=2)
        for pts, colr in ((door, (220, 30, 30)), (win, (30, 90, 230))):
            for x, y in transform(pts, c0, f['rot'], f['mirror'], k, loc): d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=colr, outline=(255, 255, 255))
        path = os.path.join(folder, f'fit_{i}.png'); im.resize((im.width * 2, im.height * 2), Image.LANCZOS).save(path)
        print(f"  {i}. score {f['score']:.2f}  rotated {f['rot']:.1f} deg{'  MIRRORED' if f['mirror'] else ''}  -> north {plan_north(f['rot'], a.arrow)}  ({path})")
    print("Open the images. Pick the fit whose outline sits on the unit, with the main door (red) at the corridor and the windows (blue) facing outside."
          "\nThen save it: add --pick N --out plan.json. If none fits, the floor plan is probably a different flat type: ask for the right page.")


if __name__ == '__main__':
    main()
