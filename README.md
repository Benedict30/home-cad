# Home CAD

A browser-based home planner for a 4-Room Type 3 HDB flat, traced from the HDB floor plan at millimetre scale.

**Open it:** https://benedict30.github.io/home-cad/

## What it does

- **Plan view** – CAD-style drawing with the plan's dimension chains, room areas, door swings and floor finishes. Structural walls are shaded black, as on the HDB plan.
- **Editing** – draw new partitions, add doors and windows, mark partitions for removal, dimension anything, and drag, rotate or resize furniture with wall snapping and clash highlighting.
- **3D and Walk** – a dollhouse model with wall-height cutaways, plus a first-person walkthrough at eye height.
- **Sun study** – sun position for Singapore by month and time of day.
- **Knock-down check** – every wall coloured by what HDB's renovation guidelines allow: partitions that can go with a permit, restricted bathroom walls, and walls that must stay.
- **Design ideas** – [Scandinavian family home](https://benedict30.github.io/home-cad/#combo-scandi), [Japandi calm](https://benedict30.github.io/home-cad/#combo-japandi), [semi-open kitchen](https://benedict30.github.io/home-cad/#combo-semiopen), [minimalist open study](https://benedict30.github.io/home-cad/#combo-minimal), [modern contemporary](https://benedict30.github.io/home-cad/#combo-modern), [industrial chic](https://benedict30.github.io/home-cad/#combo-industrial), [three generations](https://benedict30.github.io/home-cad/#combo-multigen), [family that hosts](https://benedict30.github.io/home-cad/#combo-hosting). Popular 4-room BTO styles kept practical for everyday Singapore living: each has a full-height shoe cabinet with a seat, the household shelter set up as a storeroom, and a utility cabinet in the service yard. CAD drawings of all 8: [design-ideas-cad-plans.png](https://benedict30.github.io/home-cad/design-ideas-cad-plans.png)
- **Households** – [big family](https://benedict30.github.io/home-cad/#combo-bigfamily), [gaming & cinema](https://benedict30.github.io/home-cad/#combo-gamers), [pets & aquarium](https://benedict30.github.io/home-cad/#combo-pets), [collector’s home](https://benedict30.github.io/home-cad/#combo-collectors), [work & workout](https://benedict30.github.io/home-cad/#combo-workfit), [hosts & home chefs](https://benedict30.github.io/home-cad/#combo-hostchef), [creator & music studio](https://benedict30.github.io/home-cad/#combo-studio), [elder-care home](https://benedict30.github.io/home-cad/#combo-eldercare). Homes planned around how 14 kinds of Singapore households live: large families, gamers and cinema lovers, dog and cat owners, fishkeepers, collectors, fashion lovers, fitness fans, work-from-home couples, hosts, home chefs, content creators, musicians and elder care. Pet and elder-care plans follow HDB’s pet limits and EASE fittings. CAD drawings of all 8: [households-cad-plans.png](https://benedict30.github.io/home-cad/households-cad-plans.png)
- **Out-of-the-box layouts** – [home cinema & games](https://benedict30.github.io/home-cad/#combo-cinema), [zen tatami room](https://benedict30.github.io/home-cad/#combo-zen), [jungle lounge](https://benedict30.github.io/home-cad/#combo-jungle), [glass box office](https://benedict30.github.io/home-cad/#combo-glassbox), [studio loft](https://benedict30.github.io/home-cad/#combo-loft), [wellness suite with gym & sauna](https://benedict30.github.io/home-cad/#combo-wellness), [loop house](https://benedict30.github.io/home-cad/#combo-loop), [light corridor](https://benedict30.github.io/home-cad/#combo-glasshall). Bolder ideas with glass walls, raised platforms and rooms put to new uses, still using only walls HDB lets you knock down.
- **Layouts** – [open study](https://benedict30.github.io/home-cad/#combo-a), [open dining](https://benedict30.github.io/home-cad/#combo-a-dining), [master suite](https://benedict30.github.io/home-cad/#combo-b), [study + master suite](https://benedict30.github.io/home-cad/#combo-ab), [master suite with private study](https://benedict30.github.io/home-cad/#combo-bc), [study + family area](https://benedict30.github.io/home-cad/#combo-ac), [twin kids' room](https://benedict30.github.io/home-cad/#combo-c), [home office for two](https://benedict30.github.io/home-cad/#combo-c-office). Each is furnished; step through either set on the plan, in 3D or walking.
- **Schedule** – room areas, a flooring estimate from your own rates, a furniture list, and a list of renovation changes.
- **Export** – A4 plan drawing (PNG), 3D view (PNG), project file (JSON) and schedule (CSV).

All 8 out-of-the-box layouts as CAD drawings on one sheet: [out-of-the-box-cad-plans.png](https://benedict30.github.io/home-cad/out-of-the-box-cad-plans.png)

Edits are saved in your own browser. Use Export → Project file to keep a copy or move it to another device.

## Plan your own flat

Got a different HDB flat? Get the free Claude skill at **https://benedict30.github.io/home-cad/prompt/**, add it in Claude under Customize › Skills, then attach your floor plan and say who lives with you. You get a wall-by-wall knock-down check under HDB's rules and 4 layouts for how you live, with "now" and "after" plans if a baby is coming or parents may move in, all drawn to scale.

## Notes

Room positions are traced from a photo of the HDB plan and may be off by around 100 mm in places. Check against the official plan or measure on site before ordering built-in furniture. Hacking any wall needs HDB approval; structural walls cannot be altered.

The page is a single self-contained `index.html`. It loads three.js from jsDelivr and fonts from Google Fonts.
