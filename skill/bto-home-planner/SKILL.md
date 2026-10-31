---
name: bto-home-planner
description: Use when someone shares a BTO or other HDB floor plan, or asks to plan their home or flat with one attached, and wants to know which walls they can knock down, or how to lay out the flat for how they live, such as dog owners, collectors, working from home, gaming, a baby on the way or renting out a room. Gives a wall check under HDB rules, layouts for their use cases, and a CAD app of their flat with 2D plans, 3D and a walk-through.
---

# BTO home planner

Help someone plan an HDB flat (Singapore public housing), whether a new BTO or a resale flat, from its floor plan. Focus on how they will live in it: who lives there, what changes are coming, and which walls can actually move. Don't suggest decor styles unless asked.

## 1. Get the inputs

- **Floor plan.** A photo, screenshot or PDF of the HDB plan. If it's missing, ask for it.
- **The household.** Who lives there (ages, kids, parents, a helper, pets), who works from home, and what's coming up (a baby, parents moving in, kids growing up, renting out a room). If this is missing, ask once in one short message. If they say "just go", assume a typical couple and state that assumption.
- **Must-haves**, and the block's completion date if known (it decides the 3-year bathroom rule).

Never repeat block or unit numbers from the plan in your answer or drawings.

## 2. Read the plan

- Zoom in by cropping the image if you can run code, and read the dimension chains and the legend. Don't trust where the chain ticks land: some hit wall centre-lines and some hit wall faces. Instead, scale the photo from the overall chains, measuring x and y separately because photos are often skewed, and measure each wall's centre in pixels. If horizontal lines slope or vertical lines lean, measure the slope too. Then draw your walls back onto the photo with `scripts/overlay.py` (it takes the slope as KX KY) and fix any that drift. Read every number from their photo: the demo flat built into the app is a different flat. Usable space is about 100–200 mm smaller than centre-line sizes.
- List each room with its rough size, windows and doors.
- Find:
  - the household shelter (a thick box with a heavy door)
  - the bathrooms
  - the kitchen (a dashed edge means there's no wall)
  - the service yard
  - the aircon ledge
  - the main door

## 3. Wall check

Tag every wall so the tags match the drawings: S for structural, H for the shelter, B for bathroom walls, E for external walls (even when they're shaded black), W for walls that can go, and K for open edges with no wall. Number them (S1, W1, W2…). Give one table: wall | can it go? | why. Group walls that share a type and a reason into one row (S1–S6, B1–B4) so the table stays short.

| Wall | Rule |
|---|---|
| Structural walls and columns (shaded black or marked in the legend) | Must stay. Beams stay too; a removed wall leaves a bulkhead line on the ceiling. |
| Household shelter | Must stay: walls, door, floor and ceiling. Only small screw fixings. Don't count it as a bedroom. |
| Bathroom walls and floor finishes | Can't be hacked for the first 3 years after the block is completed. After that, changes are limited and need a permit. |
| External walls, windows, main entrance wall | Must stay. |
| Other thin partitions | Can go with HDB approval through an HDB-registered (DRC) contractor. A Professional Engineer is needed if it's reinforced concrete. |

List the walls you're unsure about, and say how to check them:
- the contractor's permit application to HDB
- the wall's thickness, and a knock test
- switches, pipes and trunking inside the wall
- beams above it

If you can search the web, check HDB's current rules first.

## 4. Match layouts to the use cases

Give 4 layouts by default. At least one should knock down nothing. If hacking doesn't suit the household (they need every bedroom, say), it's fine for all 4 to keep every wall; vary how the rooms are used instead.

For each layout, give:
- the walls that come down
- what each room becomes
- the key furniture, by name (its sizes in mm go on the drawings)
- one line of pros and one line of cons

Keep walkways at least 800 mm wide. Gaps beside a bed can be narrower, down to about 550 mm.

Common sizes in Singapore, in mm (width × depth):

| Item | Size |
|---|---|
| Single / super single / queen / king bed | 900 × 1900 / 1070 × 2000 / 1530 × 1990 / 1830 × 1990 |
| Cot | 1300 × 700 |
| Wardrobe | 600 deep, any width |
| Desk | 1200–1600 × 600–700 |
| 3-seat sofa | 2000 × 900 |
| Dining table for 4 / 6 | 1400 × 800 / 1800 × 900 |
| TV console | 1400–1800 × 400 |
| Shoe cabinet with seat | 900 × 350 |
| Washer-dryer, fridge | 600 × 650, 700 × 700 |

If a life change is coming, show the layout **now** and **after** the change. If what's coming isn't a change to who lives there (more video calls, a child growing up), plan for it from day one with furniture that can change, and skip the now/after. A now/after pair counts as one layout. Give the best layout both versions. If the change affects every layout, give the others their "after" version only, and describe the "now" in one line. Prefer changes that are cheap to undo (furniture, sliding partitions) over hacking. Never knock down a wall the household will want back.

Use cases to draw on:
- **Couple, kids later:** a study or guest room now that becomes the nursery. Wardrobes that suit both uses.
- **Baby or toddler:**
  - The nursery goes next to the main bedroom.
  - A play corner instead of a coffee table.
  - Stroller space by the door.
  - Window grilles or locks.
- **Big family (3+ kids):** bunk beds, a study desk for two, a 6-seat table and lots of shoe storage.
- **Parents moving in, or ageing in place:**
  - The senior's room goes next to the common bathroom.
  - A clear 1.5 m wheelchair turning circle, 900 mm clear doorways, no rugs and night lights.
  - HDB's EASE programme subsidises grab bars, slip-resistant treatment, a foldable shower seat and ramps for households with someone 65 or older, or 60–64 and needing help with daily activities.
- **Live-in helper:**
  - Her own room if possible, with ventilation, privacy and a proper bed.
  - MOM says she must not share a room with an adult or teenage male.
- **Working from home:**
  - Put desks by a window, with a tidy video-call background.
  - If both are on calls, use separate rooms, or a bookshelf divider with the desks facing away from each other.
- **Fitness:** rubber flooring and a mirror wall. No weight drops, because the flat below hears them.
- **Pets:**
  - HDB allows 1 dog of an approved breed and up to 2 cats per flat, so never plan for more.
  - **Cats:**
    - Pet cats must be microchipped and licensed with AVS; keeping an unlicensed cat has been an offence since 1 September 2026.
    - AVS expects owners to fit mesh, grilles or screens so cats can't roam or fall. So: mesh on every window that opens, including the yard and bathroom windows, plus a mesh screen on the main gate.
    - Litter boxes go in the yard, with a cat flap or the door kept ajar.
  - The approved breeds are mostly small dogs, such as the Shih Tzu, Maltese, Pomeranian, toy poodle and miniature schnauzer. Corgis and Shiba Inus aren't on the list. Project ADORE also allows one local mixed-breed dog up to 55 cm tall. If their breed isn't on the list, say so kindly and plan for the dog anyway.
  - Scratch-resistant flooring, a pet wash tub in the yard, and gates at the kitchen.
  - Put aquariums on structural walls, and get an engineer for large tanks.
- **Hosting and cooking:**
  - A wet kitchen behind glass doors for wok cooking.
  - A dry kitchen island, pantry towers, and dining for 8 by opening up a bedroom.
- **Creators and musicians:**
  - Acoustic panels stop echo, not noise, so add door seals as well.
  - Electronic drums, and instruments on internal walls.
- **Collectors and fashion:** glass-door display cabinets, a dehumidifier for leather, and a walk-in wardrobe (often Bedroom 2 joined to the main bedroom).
- **Gaming, streaming and cinema:**
  - A projector wall, or a gaming room for two.
  - Two streamers in one room: desks back to back with a shelf between them, and dynamic or cardioid mics.
  - Gaming PCs make heat, so give that room its own aircon. Plan sockets, LAN cables and aircon trunking before the carpentry.
- **Renting out a room:**
  - Needs HDB approval.
  - A 4-room or bigger flat can rent out up to 2 of its original bedrooms.
  - Occupancy is capped at 8 people until the end of 2028, then 6.
  - Keep the rented room as an original bedroom, and check the minimum occupation period rules.
- **Empty nesters:** Bedroom 2 becomes a walk-in wardrobe or hobby room, with one guest room kept.

Everyday Singapore must-haves for any layout:
- a shoe cabinet with a seat at the door
- the shelter set up as a storeroom with free-standing racks
- utility storage in the service yard
- aircon trunking
- glass doors if they cook with a wok

## 5. Build their CAD app

Use the bundled app, `assets/home-cad.html`: a self-contained home CAD planner with a floor plan, a 3D model, a walk-through, furniture editing and export. Don't write your own drawing code.

Write the plan as a JSON file (`plan.json`). The comment above `/*PLAN-START*/` in `assets/home-cad.html` explains every field.

- **Describe the flat once:**
  - every wall, tagged as in the wall check, with its ends in mm, its thickness and its type
  - the doors and windows on each wall; give doors `hinge` and `flip` so they swing as on the plan
  - each room's outline, along the wall centre-lines
  - the fixed fittings in every layout: WC, basin, shower, kitchen counters, fridge and washer
  - optionally `start`, a point just inside the main door, if the Walk view starts in the wrong place
  Use the plan's dimension chains, so everything is to scale. Put walls on their centre-lines; the app's overall dimension is the centre-line total, so it reads a little less than the plan's outside-face figure.
- **Add one entry per layout:**
  - the walls removed, and any new walls
  - the room names for that layout
  - the furniture: centre point, width, depth, height, rotation and kind, with a plain name ("Queen bed", "Cot", "Cat tree", "Fridge"), because the name picks the 3D model
  Put the best layout first and set `best` on it (on both entries if it has a now and an after). For a life change, add separate "now" and "after" entries. If several layouts share the same "now", add it once.
- **Check it fits:** run `python3 scripts/check_plan.py plan.json`. It flags any piece outside its room, in a wall, in a door swing or on another piece. Fix everything it lists and run it again until it says OK. Also check by eye that walkways stay at least 800 mm wide and beds have their headboard against a wall.
- **Build the app:** run `python3 scripts/build_app.py plan.json`. It checks the plan's format, puts it into the app and saves the file where you can share it (on claude.ai, `/mnt/user-data/outputs/`). Share that file. Don't retype the app into an artifact: it's about 1 MB, with the 3D engine built in.
- Tell them to download the file and open it in any browser, on a phone or a computer; it works offline. It opens on the layouts, best fit first, with arrows to step through them in Plan, 3D and Walk. **Knock down** colours each wall by what HDB allows and shows the same tags as your wall check. They can move furniture, try their own changes and export a plan drawing.

## 6. Reply

- Keep the chat reply short and easy to scan: tables and brief bullets.
- Give each layout 3–4 lines in chat. Put furniture sizes and positions in the drawings, not the reply. The room list from step 2 can stay out of the reply too.
- Put a 2–3 line summary first: the best layout for them and why.
- Then one line about the CAD app file: download it and open it in a browser to step through the layouts in 2D, 3D and walking.
- End with what to confirm with HDB or the contractor before any hacking:
  - permit and Professional Engineer needs
  - the block's completion date
  - services inside the walls
  - beams
  - measurements taken on site
- Remind them you've read a photo, so they should check against the official plan.
