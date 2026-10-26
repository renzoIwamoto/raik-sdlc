---
name: raik-product
description: Defines what the product is and for whom. Use when starting a product, when its scope, users or voice are unclear, or when user stories need writing, splitting or acceptance criteria. Produces a vision, a PRODUCT.md with users, voice and principles for design, and user stories with stable IDs, MVP or Later tags and concrete Given/When/Then criteria.
---

# raik-product

Every later decision traces back to these documents. Keep them short, concrete and current.

## When to use

- A new product or a major pivot.
- A feature whose user value or acceptance criteria are unclear.
- Before `raik-design` (it reads `PRODUCT.md`) and before a phase plan.

## Steps

### 1. Interview

Use `raik-decide` rounds to learn: the problem and who has it, what they do today, the promise, what the product will **not** do, the scope (market, platforms, languages), and how success will be measured. Research facts yourself (competitors, regulations, platform limits) and cite them.

### 2. Write the vision

`docs/vision.md`: problem, users, promise in one sentence, non-goals, scope now and later, success measures with numbers, and the biggest risks.

### 3. Write PRODUCT.md

The brief that design and copy follow. Template: `assets/product-template.md`. Users and their context, voice and tone with examples of good and bad copy, design principles (three to five, each a choice that rules something out), anti-references, and accessibility commitments.

### 4. Write user stories

`docs/product/user-stories.md`, grouped by epic, in `docs_language`. Format in `assets/user-story-template.md`:

- Stable IDs (`US-01`, `US-02`...). Never renumber or reuse an ID; retired stories are marked, not deleted.
- Each story tagged `MVP` or `Later` and with the phase that delivers it.
- Every MVP story has acceptance criteria in Given/When/Then with **concrete values** ("a S/ 100 purchase in September and a S/ 40 refund in October"), including the unhappy paths and edge cases.
- A criterion that cannot be tested is rewritten until it can.

### 5. Check consistency

Stories against the vision's non-goals, against domain rules, and against each other. Report contradictions instead of resolving them silently.

## Gates

- G1: scope, priorities and non-goals are the user's decisions.
- No MVP story without testable criteria.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "Acceptance criteria can come with the spec." | The spec derives from them. Vague criteria make vague specs. |
| "Non-goals are negative, skip them." | Non-goals stop scope creep and settle half the future debates. |
| "IDs can be renumbered to stay tidy." | Other documents and commits reference them. Never renumber. |
| "The voice section is fluff." | It decides every label, error and empty state. Give examples. |

## Output

`docs/vision.md`, `PRODUCT.md` and `docs/product/user-stories.md`, plus the open questions left for later rounds.
