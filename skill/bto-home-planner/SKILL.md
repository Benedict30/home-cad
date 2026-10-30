---
name: bto-home-planner
description: Use when someone shares a BTO or other HDB floor plan, or asks to plan their home or flat with one attached, and wants to know which walls they can knock down, or how to lay out the flat for how they live, such as dog owners, collectors, working from home, gaming, a baby on the way or renting out a room. Gives a wall check under HDB rules, layouts for their use cases, and floor plans with a 3D view they can walk through.
---

# BTO home planner

Help someone plan an HDB flat (Singapore public housing), whether a new BTO or a resale flat, from its floor plan. Focus on how they will live in it: who lives there, what changes are coming, and which walls can actually move. Don't suggest decor styles unless asked.

## 1. Get the inputs

- **Floor plan.** A photo, screenshot or PDF of the HDB plan. If it's missing, ask for it.
- **The household.** Who lives there (ages, kids, parents, a helper, pets), who works from home, and what's coming up (a baby, parents moving in, kids growing up, renting out a room). If this is missing, ask once in one short message. If they say "just go", assume a typical couple and state that assumption.
- **Must-haves**, and the block's completion date if known (it decides the 3-year bathroom rule).

Never repeat block or unit numbers from the plan in your answer or drawings.

## 2. Read the plan

- Zoom in by cropping the image if you can run code, and read the dimension chains and the legend. The inner chains run to wall centre-lines, so usable space is about 100–200 mm smaller. The overall chains usually run to the outside faces of the external walls, so they're a wall thickness bigger than the centre-line total.
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

Keep walkways at least 800 mm wide.

If a life change is coming, show the layout **now** and **after** the change. If what's coming isn't a change to who lives there (more video calls, say), plan for it from day one and skip the now/after. A now/after pair counts as one layout. Give the best layout both versions. If the change affects every layout, give the others their "after" version only, and describe the "now" in one line. Prefer changes that are cheap to undo (furniture, sliding partitions) over hacking. Never knock down a wall the household will want back.

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
- **Gaming and cinema:** a projector wall, a gaming room for two, and cable runs planned before the carpentry.
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

## 5. Draw the plans in 2D and 3D

Use the bundled viewer, `assets/plan-viewer.html`. Don't write your own drawing code.

- Copy the file exactly and replace only the JSON between `/*PLAN-START*/` and `/*PLAN-END*/`. The comment above it explains every field.
- **Describe the flat once:**
  - every wall, tagged as in the wall check, with its ends in mm, its thickness and its type
  - the doors and windows on each wall; give doors `hinge` and `flip` so they swing as on the plan
  - each room's outline
  - optionally `start`, a point just inside the main door, if the Walk view starts in the wrong place
  Use the plan's dimension chains, so everything is to scale. Put walls on their centre-lines; the viewer's overall dimension is the centre-line total, so it reads a little less than the plan's outside-face figure.
- **Add one entry per layout:**
  - the walls removed, and any new walls
  - the room names for that layout
  - the furniture: centre point, width, depth, height, rotation and kind
  Put the best layout first and set `best` on it (on both entries if it has a now and an after). For a life change, add separate "now" and "after" entries. If several layouts share the same "now", add it once.
- **Check the furniture fits:**
  - every piece stays inside its room, clear of walls and door swings
  - walkways stay at least 800 mm wide
  - beds have their headboard against a wall
- Publish the result as an HTML artifact. It shows:
  - a 3D model people can turn, or walk through at eye height with a small floor plan showing where they are, with a button for each layout
  - a wall key
  - each layout's floor plan next to a 3D snapshot
  The wall colours and the legend are built in.

## 6. Reply

- Keep the chat reply short and easy to scan: tables and brief bullets.
- Give each layout 3–4 lines in chat. Put furniture sizes and positions in the drawings, not the reply. The room list from step 2 can stay out of the reply too.
- Put a 2–3 line summary first: the best layout for them and why.
- End with what to confirm with HDB or the contractor before any hacking:
  - permit and Professional Engineer needs
  - the block's completion date
  - services inside the walls
  - beams
  - measurements taken on site
- Remind them you've read a photo, so they should check against the official plan.
