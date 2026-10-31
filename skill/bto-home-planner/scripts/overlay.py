"""Draw your walls back onto the floor plan photo to check they line up.
Usage: python3 overlay.py plan.json photo.jpg out.png X0 Y0 SX SY
X0 Y0 = the pixel where plan point (0, 0) sits; SX SY = pixels per mm across and down (measure them separately: photos are often skewed)."""
import json, sys
from PIL import Image, ImageDraw
plan = json.load(open(sys.argv[1])); im = Image.open(sys.argv[2]).convert('RGB'); x0, y0, sx, sy = map(float, sys.argv[4:8])
d = ImageDraw.Draw(im); P = lambda p: (x0 + p[0] * sx, y0 + p[1] * sy)
COL = {'structural': (220, 30, 30), 'shelter': (220, 30, 30), 'bathroom': (230, 140, 0), 'external': (30, 90, 230), 'partition': (20, 160, 70), 'open': (150, 150, 150)}
for w in plan['walls']:
    d.line([P(w['a']), P(w['b'])], fill=COL.get(w['type'], (0, 0, 0)), width=max(2, int((w.get('t') or 120) * sx * .5)))
    m = P(((w['a'][0] + w['b'][0]) / 2, (w['a'][1] + w['b'][1]) / 2)); d.text((m[0] + 3, m[1] + 3), w['id'], fill=(0, 0, 0))
im.save(sys.argv[3]); print('Wrote', sys.argv[3], '- walls should sit on the drawn walls; fix any that drift.')
