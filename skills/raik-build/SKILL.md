---
name: raik-build
description: Implements the tasks of an approved change. Use when a change is approved and its tasks need coding, or when the user asks to implement, code or fix something already specified. Applies the project's stack profile, test-driven development for domain rules and money, business rules as named functions in one place, boundaries checked as it goes, and the project's working mode (the agent implements, or guides the user to implement).
---

# raik-build

Build exactly what the change says, in small verified steps, inside the architecture's boundaries.

## When to use

- After `raik-change` is approved (gate G2).
- For trivial edits exempt from G2 (typos, versions, styling), with the same quality rules.

## Steps

### 1. Load the contract

Read the change: proposal (scope and out of scope), design (decisions), spec (scenarios) and tasks. Load the stack profile from the `raik-architecture` skill (`references/profile-*.md`). Read the code you will touch and every caller of the functions you will change.

### 2. Work task by task, in order

For each task:

1. **Test first** for domain rules, money, parsing, permissions and anything with branches: write the test that fails, named after the rule or scenario; make it pass with the minimum code; refactor. Run it and see it fail before the fix and pass after.
2. **One home per rule.** A business rule is a named function in the domain (`needs_category`, `net_spend`), called from every place that needs it. Never repeat the condition inline in two places.
3. **Fix at the shared point.** A bug in a function used by many callers is fixed in that function, once, not patched in the caller that reported it.
4. **Respect the boundaries.** Run the boundary check (`lint-imports` or equivalent) when you touch imports.
5. **UI tasks** follow `raik-ui`.
6. Run the unit tests and type checks for what you touched. An unexpected failure goes to `raik-debug`; do not guess-fix.
7. Mark the task implemented. It is checked only by `raik-verify`, with evidence.

### 3. Keep the change truthful

When implementation shows a decision must change, update the change's `design.md` ("Adjusted during implementation: <what and why>") and tell the user if it changes behavior or scope.

### 4. Working mode

- `ai-implements`: write the code; explain non-obvious choices in a sentence.
- `user-implements`: propose the failing test and the next small step; let the user write the code; review with hints before full solutions. Mechanical work (config, commands, docs) you may do when asked.
- `pair`: ask per task.

## Rules

- No new dependency without saying why and which alternative was rejected; prefer the standard library and what is already installed.
- Code, identifiers and comments in `code_language`. Comments explain why, not what.
- No secrets, tokens, personal data or full card numbers in code, tests, fixtures or logs. Fixtures from real data are anonymized first.
- Write files with LF line endings and UTF-8; let `.gitattributes` normalize.
- Generated code (API clients, migrations) is regenerated, not hand-edited.

## Gates

- G2: no build without an approved change, except the exempt trivial edits.
- No task marked implemented with failing tests or type errors.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "I'll add tests after it works." | Then the test is shaped by the code, not the rule. Test first for rules. |
| "The same check in two places is fine for now." | The two copies will disagree. Extract the rule. |
| "Quick fix in the caller." | Other callers keep the bug. Fix the shared function. |
| "This import crosses a boundary, but just once." | Boundaries erode one exception at a time. Go through the public API. |
| "I'll leave the design.md as it was." | A design that no longer matches the code misleads the reviewer. Update it. |

## Output

Code and tests for each task, tasks marked implemented, any design adjustments noted, and the test and type-check results.
