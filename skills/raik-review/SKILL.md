---
name: raik-review
description: Reviews a diff before it ships, through four lenses - correctness, tests, security and simplicity. Use after verification and before shipping, when the user asks for a code or security review, or when a change touches authentication, authorization, user data, money, infrastructure or dependencies. Reports only findings it has confirmed, ranked by severity, each with file and line, the failure scenario and the fix, and runs the available scanners for secrets, dependencies and static analysis.
---

# raik-review

A review finds what the author could not see. It is only useful if every finding is real and actionable.

## When to use

- After `raik-verify`, before `raik-ship`.
- Mandatory when the diff touches authentication, authorization or row-level policies, personal or financial data, secrets, infrastructure, or adds a dependency.
- When the user asks for a review of a branch, PR or diff.

## Steps

### 1. Scope

Get the diff against the target branch (`git diff <base>...HEAD`) and read the change's spec and design. Review what changed and what it touches, not the whole repo.

### 2. Review through four lenses

Use the checklists in `references/checklists.md`, one lens at a time:

| Lens | Asks |
|---|---|
| Correctness | Does the code do what the spec says in every scenario, including empty, error and boundary values? |
| Tests | Does each scenario and rule have a test that would fail if the code broke? |
| Security | Can an input, user or dependency make it leak, corrupt or escalate? |
| Simplicity | Is there code to delete, a duplicate rule, an abstraction with one use, a dependency the standard library replaces? |

### 3. Run the scanners that exist

Use what the project and the machine have, and say what was not available:
- Secrets: `gitleaks detect` (or the project's scanner).
- Dependencies: `pip-audit`, `pnpm audit` / `npm audit`.
- Static analysis: `semgrep --config auto`, CodeQL in CI, `ruff` with security rules.
- If the agent offers built-in review commands (for example a security review), they may add findings; treat them like any other: confirm before reporting.

### 4. Confirm before reporting

For each candidate finding, trace the code path and confirm the failure scenario is real. Drop what you cannot confirm, or label it clearly as a question. No speculative findings.

### 5. Report

Ranked by severity (critical, high, medium, low), each with: `file:line`, the problem in one sentence, the concrete failure scenario (input or state → wrong result), and the fix. Group simplicity suggestions separately; they are not bugs.

### 6. Fix per mode

In `ai-implements`, fix confirmed findings that are inside the change's scope, then re-run `raik-verify`. Findings outside scope become follow-ups for the user to decide. In `user-implements`, report and let the user fix.

## Gates

- A change touching auth, user data or infrastructure does not ship without the security lens.
- Fixes are verified like any other code (G3).

## Excuses

| Excuse | Rebuttal |
|---|---|
| "Tests pass, so it's correct." | Tests check what was imagined. Read the code against the spec. |
| "Report everything, the user can filter." | Unconfirmed findings waste time and bury the real ones. Confirm first. |
| "The scanner isn't installed, skip security." | Do the security checklist by hand and say which scanner is missing. |
| "That refactor would be nice too." | Out of scope. Suggest it as a follow-up; do not grow the change. |

## Output

A ranked list of confirmed findings with fixes, the scanners run and their results, what was fixed, and follow-ups for the user.
