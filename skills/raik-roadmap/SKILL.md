---
name: raik-roadmap
description: Plans the work in phases with measurable checkpoints and keeps the plan honest. Use when planning or replanning phases, deciding what comes next, slicing work into vertical changes, recording progress, or checking whether a phase can close. Produces a roadmap with one checkpoint per phase, dated progress entries with evidence, and a phase-close review that maps every story to its evidence or its gap.
---

# raik-roadmap

A roadmap is useful only if it says where the project really is. Phases close on evidence, not on effort.

## When to use

- After product, domain and architecture are drafted: plan the phases.
- `raik next` needs to know what comes next.
- A change finishes and the roadmap must record it.
- Someone asks "is this phase done?".

## Steps

### 1. Plan phases

`docs/roadmap.md` with a table: phase | content | **checkpoint** | status. Template: `assets/roadmap-template.md`.

- A checkpoint is observable and binary: "a real bank email produces a transaction in the database without intervention", not "ingestion works".
- Order phases so each delivers something usable or removes the biggest risk next.
- A line at the top says the current phase.
- Open questions are listed with the phase that will answer them.

### 2. Slice into changes

Split a phase into vertical changes: each one is end to end (data, logic, UI, tests) and leaves the product working. Prefer several small changes over one large one. Each becomes a `raik-change`.

### 3. Record progress

After each shipped change, add a dated entry under the current phase: what changed, the evidence (tests, e2e counts, screenshots), the limits of that evidence, and what remains. Link the change. Never write "done" without the evidence.

### 4. Review a phase before closing it

Write a phase-close review (template in `assets/roadmap-template.md`): a table mapping each story or deliverable of the phase to its evidence or its gap. Then:

- No gaps: propose closing the phase; the user confirms.
- Gaps: list them; either schedule them in this phase or, if the user decides, move them to a later phase with the reason recorded. Do not remove a checkpoint criterion to make a phase look done.

## Gates

- G1: changing scope, order or checkpoints of phases is the user's decision.
- G3: a phase closes only with evidence for every item, or with gaps the user explicitly deferred.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "The checkpoint is basically met." | Basically is a gap. List what is missing. |
| "I'll update the roadmap at the end of the phase." | Progress written later is reconstructed and wrong. Record it per change. |
| "This deferred item can just be dropped." | Dropping scope is a decision; ask and record it. |
| "One big change for the whole phase is simpler." | Big changes hide progress and risk. Slice vertically. |

## Output

An updated `docs/roadmap.md`: phases with checkpoints, the current phase, dated progress with evidence, and, when asked, a phase-close review with the gaps.
