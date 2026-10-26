---
name: raik-decide
description: Runs decision rounds before work starts. Use when a plan, feature, design or architecture choice has open questions or trade-offs, when the user asks to be questioned about a plan, or when they say "decide for me". Asks numbered questions with a recommendation each, in rounds ordered by dependency, lets the user delegate, and records every decision in the document where it belongs.
---

# raik-decide

Turn open questions into recorded decisions, with as little of the user's time as possible.

## When to use

- Before `raik-change`, when the change has choices the user should make.
- When the user brings an idea or plan and wants it stress-tested.
- When docs contradict each other or the code, and someone must choose.

Not for facts. Anything you can learn by reading the code, the docs or the web, you find yourself.

## Steps

### 1. Gather the facts

Read the relevant docs, code and prior decisions (ADRs, domain rules, design system). Research outside facts when needed and cite them. List contradictions you find; they become questions.

### 2. Build the decision tree

Write down every decision the work needs and what each depends on. The **frontier** is every decision whose prerequisites are already settled. Ask only the frontier; a question that depends on another open question waits for the next round.

### 3. Ask one round

Use this format, in `docs_language`:

```
**Q1 - <short title>**: <the question, with the options when there are several>
➡️ <your recommendation and why, in one or two sentences>

---

**Q2 - ...**
```

Rules for a round:
- At most eight questions. Number them so the user can answer "1 yes, 2 b, 3 your call".
- Every question carries a recommendation. A question without one pushes your work onto the user.
- Mark questions that are expensive to reverse (data model, public API, licensing, anything published).
- Say what happens if the user does not care: "if you don't mind, I'll go with X".
- Put facts first and the question last; keep each question readable on its own.

### 4. Take the answers

- Explicit answer: apply it.
- "Decide for me", "your call", "whatever you think is best": apply your recommendations and **list each choice in one line** in your reply, so the user can still object.
- Partial answer: apply what was answered; carry the rest to the next round with the remaining frontier.
- An answer that conflicts with a document or an earlier decision: point out the conflict and ask which one wins.

### 5. Record each decision where it lives

| Kind of decision | Where it goes |
|---|---|
| Product scope, users, priorities | `PRODUCT.md`, user stories, roadmap |
| Business rule | domain doc (numbered rule) and the glossary |
| Architecture, stack, infrastructure | a **new** ADR; never edit an accepted one, supersede it |
| Visual or interaction design | `DESIGN.md` |
| How the team works | `AGENTS.md` |
| Scope of one change | that change's `design.md` (Decisions section) |

Each recorded decision says what was decided, why, and the date. When the user delegated, say so ("decided by the assistant with the user's authorization").

### 6. Repeat until the frontier is empty

Recompute the frontier after each round. Stop when every branch is decided or explicitly deferred, then confirm the shared understanding in a few lines before any work starts.

## Gates

- Do not start building while a frontier question is open, unless the user said to proceed with your recommendations.
- Do not record a recommendation the user did not accept as a decision. Keep it as pending.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "I'll just pick the obvious option." | Then it is cheap to ask: recommend it and let the user confirm in one word. |
| "Asking twelve questions at once saves time." | Questions that depend on unanswered ones get answered twice. Ask the frontier only. |
| "I need to ask what the code does." | Read the code. The user decides; you find facts. |
| "The user said 'decide for me', so no need to report." | Delegation still needs a list of what you chose, or it cannot be reviewed. |
| "This decision is small, no need to write it down." | If it changes behavior or structure, someone will ask why. Record it in one line. |

## Output

A round of numbered questions with recommendations, or, once settled, a short list of decisions with where each was recorded.
