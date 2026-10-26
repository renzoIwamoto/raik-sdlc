---
name: raik-design
description: Sets the visual direction and the design system of a product. Use when a product needs its look and feel defined, when the design system (tokens, type, color, components, motion, data visualization) is created or changes, or when screens feel inconsistent. Produces DESIGN.md and tokens in code as the single source of truth, with contrast verified by script and key screens prototyped and reviewed in screenshots. Uses Impeccable when installed.
---

# raik-design

A design system is a set of decisions that make every later screen faster and more consistent. Decide them once, write them down, encode them as tokens.

## When to use

- After `raik-product` (it reads `PRODUCT.md`): a new product needs a direction.
- The design system changes: new color, type scale, component, chart style.
- Screens drift apart and need a common rule.

For building or polishing a single screen, use `raik-ui`.

## Steps

### 1. Read the brief

`PRODUCT.md`: users and their context, voice, principles, anti-references, accessibility commitments. If they are missing, run `raik-product` first; a design without a brief is decoration.

### 2. Choose the direction

If Impeccable is installed (`design.skills` includes it), use it to shape the direction and generate the design context; follow its process for comps and critique.

Otherwise: propose two or three directions, each in a few lines (mood, type, color logic, density, one reference), mocked on the most important screen. The user chooses (gate G1). Record the reasons for the choice and for what was rejected.

### 3. Define the system

Write `DESIGN.md` with the sections in `references/design-system.md`: principles, color tokens with roles, type scale, spacing and radii, elevation policy, components and their states, motion, iconography, data visualization, and accessibility rules. Every value has a role ("action", "ink-soft"), never only a hue.

Encode the tokens in code as the only source (CSS custom properties or the Tailwind theme). Components use tokens, never literal values.

### 4. Check it

- Contrast of every text and UI token pair, by script, not by eye:
  ```bash
  python <raik-ui skill>/scripts/contrast.py --tokens <tokens.css> ink paper ink-soft paper on-action action
  ```
  AA: 4.5:1 for text, 3:1 for large text and UI parts. Fix failures in the tokens.
- Category colors in charts: distinguishable for common color vision deficiencies, and never the only carrier of meaning.

### 5. Prototype the key screens

Build the two or three screens that carry the product, with realistic data, through `raik-ui`. Review screenshots at mobile and desktop; adjust the system, not each screen.

### 6. Keep it alive

When a screen needs something the system lacks, add it to the system first (with its states), then use it. Note in `DESIGN.md` what changed and why.

## Gates

- G1: the direction and any change to brand-level choices (palette, type, tone) are the user's.
- No token pair used for text below AA.
- No literal colors or sizes in components.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "We'll define the system after a few screens." | Then each screen invents its own. Define the core now; extend later. |
| "The contrast looks fine." | Eyes and monitors lie. Run the script. |
| "This one screen needs a special color." | Add a role to the system or reuse one. One-offs become the system by accident. |
| "Charts can use any palette." | Data colors carry meaning. Define them, test them for color blindness, pair them with labels. |

## Output

`DESIGN.md`, tokens in code, the contrast report, and screenshots of the prototyped key screens with the decisions they confirmed.
