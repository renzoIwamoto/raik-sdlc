---
name: raik-ui
description: Builds and refines screens to the design system with production-level UX. Use when creating a screen or component, improving one that looks or behaves poorly, adding states (loading, empty, error, limit), or preparing UI for review. Enforces required states, accessibility (contrast by script, focus, labels, 44 px targets), responsive layout at 360 and 1440 px, and rounds of screenshot review. Uses Impeccable, Vercel Web Design Guidelines and the shadcn skill when installed.
---

# raik-ui

A screen is done when every state is designed, everyone can use it, and it was looked at on a phone and a desktop.

## When to use

- A task in a change creates or changes a screen or component.
- A screen feels off, inconsistent or hard to use.
- Before `raik-verify` on UI work.

Direction and system-level decisions belong to `raik-design`.

## Steps

### 1. Read the contract

`DESIGN.md` (tokens, components, rules), `PRODUCT.md` (voice), the story and the change's scenarios. If the design system lacks something this screen needs, add it there first.

### 2. Inventory the states

Before building, list every state of the screen using `references/screen-states.md`: loading, empty, partial, error, limit, offline when relevant, success feedback, and each state of each control. Unreachable controls are not drawn. Write the copy for each state in the product's voice.

### 3. Build

- Components from the design system; tokens only, no literal colors or sizes.
- With shadcn/ui, use the shadcn skill when installed so components and props are real.
- Semantic HTML first: buttons are `button`, links are `a`, lists are lists, headings are in order.
- Every control has an accessible name; icons alone get a label.
- Focus is visible; the keyboard path follows the visual order; dialogs trap and return focus.
- Touch targets at least 44 px; text at least 16 px in inputs (avoids zoom on mobile Safari).
- Feedback appears **where the user is looking**. After an action that moves focus or closes a sheet, check the message is still on screen.
- Respect `prefers-reduced-motion`.

### 4. Check

- Contrast of any new color pair: `python scripts/contrast.py --tokens <tokens.css> <fg> <bg>`.
- If installed, run the Web Design Guidelines audit on the changed files and fix what applies.
- If installed, use Impeccable to critique and polish.
- Screenshots at 360×800 and 1440×1000 of each state (via `raik-verify`, `references/screenshots.md` there). Look at every one.

### 5. Iterate at most twice

Fix material issues found in the check, re-take screenshots, and stop after a second round unless the user asks for more. Record what changed in the design brief when the project keeps one per screen.

## Gates

- No screen ships without its empty, error and loading states designed.
- No text pair below WCAG AA.
- No horizontal scroll at 360 px.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "The empty state is rare." | Every new user sees it first. Design it with a next step. |
| "Errors will show the API message." | API messages are for developers. Say what happened and what to do, in the product's voice. |
| "It looks right on my screen." | Check 360 px and a keyboard. Most UI bugs live there. |
| "Disabled buttons explain themselves." | Say why something is unavailable, or do not show it. |
| "Polish later." | Later the screen has users. Two short rounds now. |

## Output

The screen with all states, the contrast results, the audit findings addressed, and screenshots at both viewports.
