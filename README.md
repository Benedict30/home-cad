# Home CAD

A browser-based home planner for a 4-Room Type 3 HDB flat, traced from the HDB floor plan at millimetre scale.

**Open it:** https://benedict30.github.io/home-cad/

## What it does

- **Plan view** – CAD-style drawing with the plan's dimension chains, room areas, door swings and floor finishes. Structural walls are shaded black, as on the HDB plan.
- **Editing** – draw new partitions, add doors and windows, mark partitions for removal, dimension anything, and drag, rotate or resize furniture with wall snapping and clash highlighting.
- **3D and Walk** – a dollhouse model with wall-height cutaways, plus a first-person walkthrough at eye height.
- **Sun study** – sun position for Singapore by month and time of day.
- **Knock-down check** – every wall coloured by what HDB's renovation guidelines allow: partitions that can go with a permit, restricted bathroom walls, and walls that must stay.
- **Out-of-the-box layouts** – [home cinema & games](https://benedict30.github.io/home-cad/#combo-cinema), [zen tatami room](https://benedict30.github.io/home-cad/#combo-zen), [jungle lounge](https://benedict30.github.io/home-cad/#combo-jungle), [glass box office](https://benedict30.github.io/home-cad/#combo-glassbox), [studio loft](https://benedict30.github.io/home-cad/#combo-loft), [wellness suite with gym & sauna](https://benedict30.github.io/home-cad/#combo-wellness), [loop house](https://benedict30.github.io/home-cad/#combo-loop), [light corridor](https://benedict30.github.io/home-cad/#combo-glasshall). Bolder ideas with glass walls, raised platforms and rooms put to new uses, still using only walls HDB lets you knock down.
- **Practical layouts** – [open study](https://benedict30.github.io/home-cad/#combo-a), [open dining](https://benedict30.github.io/home-cad/#combo-a-dining), [master suite](https://benedict30.github.io/home-cad/#combo-b), [study + master suite](https://benedict30.github.io/home-cad/#combo-ab), [master suite with private study](https://benedict30.github.io/home-cad/#combo-bc), [study + family area](https://benedict30.github.io/home-cad/#combo-ac), [twin kids' room](https://benedict30.github.io/home-cad/#combo-c), [home office for two](https://benedict30.github.io/home-cad/#combo-c-office). Each is furnished; step through either set on the plan, in 3D or walking.
- **Schedule** – room areas, a flooring estimate from your own rates, a furniture list, and a list of renovation changes.
- **Export** – A4 plan drawing (PNG), 3D view (PNG), project file (JSON) and schedule (CSV).

All 8 out-of-the-box layouts as CAD drawings on one sheet: [out-of-the-box-cad-plans.png](https://benedict30.github.io/home-cad/out-of-the-box-cad-plans.png)

Edits are saved in your own browser. Use Export → Project file to keep a copy or move it to another device.

## Notes

Room positions are traced from a photo of the HDB plan and may be off by around 100 mm in places. Check against the official plan or measure on site before ordering built-in furniture. Hacking any wall needs HDB approval; structural walls cannot be altered.

The page is a single self-contained `index.html`. It loads three.js from jsDelivr and fonts from Google Fonts.
