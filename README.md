# Home CAD

Plan your BTO with AI. This repo has a free Claude skill for any BTO or resale HDB floor plan, and a 3D planner built for one 4-Room Type 3 BTO flat.

**See real results:** https://benedict30.github.io/home-cad/examples/

## Plan your own flat with the free skill

1. **Download the skill:** [bto-home-planner.zip](https://github.com/Benedict30/home-cad/raw/main/skill/bto-home-planner.zip)
2. **Add it to Claude:** go to **Customize › Skills**, click **+**, then **Create skill › Upload a skill**. Choose the ZIP and switch it on. Skills need code execution, so turn on **Code execution and file creation** in **Settings › Capabilities**.
3. **Send your floor plan** with a clear photo of your HDB plan attached, and a few lines about your home (must-haves are optional):

```
Plan my BTO. Floor plan attached.
We are: couple, no kids, 1 Shih Tzu
Coming up: more work from home
Must-haves: a dog wash spot
```

You get:
- a wall-by-wall knock-down check under HDB's rules
- 4 layouts for how you live, with "now" and "after" plans if a change is coming
- every layout drawn to scale, with a 3D model you can turn or walk through
- a short list of things to confirm with HDB and your contractor before any hacking

It works for dog owners, hardcore collectors, couples who both work from home, gamers, a baby on the way, parents moving in, big families, a live-in helper, a home gym, hosting and cooking, creators and musicians, renting out a room, and kids moving out.

The skill is plain text plus one drawing template. Read [SKILL.md](skill/bto-home-planner/SKILL.md) and [plan-viewer.html](skill/bto-home-planner/assets/plan-viewer.html) before adding it.

<details>
<summary>Not using Claude skills? Paste this prompt with your floor plan instead.</summary>

```
I've attached the floor plan of my BTO flat. Help me plan how we'll live in it.
We are: [e.g. couple, both work from home, 1 cat]
Coming up: [e.g. baby next year, my mum may move in]
Must-haves: [e.g. a proper home office]

1. Read the plan: rooms with rough sizes, windows, the household shelter, kitchen, service yard and bathrooms.
2. Wall check: for every internal wall, say if it can be knocked down under HDB's rules. Structural and shelter walls stay. Bathroom walls can't be hacked for 3 years after the block is completed. Other partitions need HDB approval and an HDB-registered (DRC) contractor, plus a Professional Engineer if they're reinforced concrete. Flag any walls you're unsure about.
3. Give me 4 layouts for how we live, including one with no hacking. If something is coming up, show the layout now and after. For each: walls down, what each room becomes, furniture with sizes in mm, pros and cons.
4. Draw each layout to scale: must-stay walls in black, walls that can go in green, removed walls in dashed green, furniture as labelled boxes.

End with what to confirm with HDB or my contractor before any hacking.
```

</details>

**Before you hack anything:** AI can misread a photo. Check every wall against your official HDB floor plan, and get HDB's approval and an HDB-registered (DRC) contractor before any work starts.

## The 3D planner

A browser-based home planner for a 4-Room Type 3 HDB flat, traced from the HDB floor plan at millimetre scale.

**Open it:** https://benedict30.github.io/home-cad/

### What it does

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

## Notes

Room positions are traced from a photo of the HDB plan and may be off by around 100 mm in places. Check against the official plan or measure on site before ordering built-in furniture. Hacking any wall needs HDB approval; structural walls cannot be altered.

The page is a single self-contained `index.html`. It loads three.js from jsDelivr and fonts from Google Fonts.
