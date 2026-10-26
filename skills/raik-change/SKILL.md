---
name: raik-change
description: Specifies a change before any code is written, using OpenSpec. Use when the user wants to add or change behavior that is more than a typo, version bump or styling tweak; when a roadmap gap or user story needs implementing; or when an existing change needs its proposal, design, spec or tasks updated. Produces a proposal, a design with numbered decisions, a spec whose scenarios are the test plan, and tasks with verification commands and evidence slots.
---

# raik-change

A change is the contract between what the user wants and what gets built. Its scenarios become the tests; its tasks become the evidence.

## When to use

- New behavior, a behavior change, or closing a gap in a user story.
- Updating a change that is not archived yet.

Skip for typos, dependency bumps and styling with no behavior change (gate G2 exemption).

## Prerequisites

- OpenSpec installed globally: `npm install -g @fission-ai/openspec`.
- Run `openspec --version`. If it differs from `changes.version` in the raik config, report the mismatch and continue.
- The project has an `openspec/` folder. If it does not, stop and offer `openspec init`; never create it as a side effect.

## Steps

### 1. Understand before writing

Read, in this order: the roadmap and phase review, the user stories and domain rules involved, existing specs (`openspec/specs/`), and active changes (`openspec list`). Then read the code the change will touch. Note what exists today, precisely, because the proposal must separate it from what is proposed.

### 2. Settle open questions

If the change has choices the user should make, run `raik-decide` first. Do not write the design with guesses.

### 3. Create the change

Name it verb-first in kebab case, describing the outcome: `show-net-spend`, `apply-rule-to-existing`. Then:

```bash
openspec new change <name>
```

### 4. Write the four artifacts

Write in `docs_language` (keep OpenSpec headings and SHALL/MUST in English). Detail and templates: `references/artifacts.md`.

- **proposal.md**: status line; Why (the stories or rules it serves, with links); What Changes; Capabilities (new or modified); Impact (files expected, and an explicit **out of scope** list).
- **design.md**: Context (what the code does today), Goals and Non-Goals, numbered **Decisions** with the reason for each, Risks and trade-offs, Migration plan.
- **specs/<capability>/spec.md**: requirements with SHALL, each with at least one scenario in WHEN/THEN. Every scenario must be checkable by a test or a script; if you cannot imagine the assertion, rewrite the scenario.
- **tasks.md**: numbered, small, ordered. Each task says who does it (per `mode`), what to change and **how it will be verified** (the command or check). Leave room for an `Evidence:` note, filled in by `raik-verify`.

### 5. Validate

```bash
openspec validate <name> --strict
```

Fix every error. Then check the links you wrote resolve.

### 6. Present and stop

Summarize in `docs_language`: what will change, the decisions (flag any you made on the user's behalf), what is out of scope, and the task count. Stop for approval before building (gate G2), unless the user already said to go ahead.

## Gates

- No `raik-build` until the change validates and the user approved it (or asked you to continue).
- Every scenario maps to a planned check; every task has a verification step.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "The design is obvious, I'll skip design.md." | Write the decisions anyway; a reviewer will ask why, and the answer belongs in the change. |
| "Scenarios can be vague; tests will be precise." | Vague scenarios produce tests that check nothing. Make them assertable now. |
| "Out of scope is implied." | Write it down. Unwritten scope grows. |
| "I'll describe current behavior from memory." | Read the code. Proposals built on assumptions describe a product that does not exist. |
| "validate passed, so the change is good." | Validation checks structure, not sense. Re-read it as the person who will implement it. |

## Output

A validated change folder and a short summary for approval.
