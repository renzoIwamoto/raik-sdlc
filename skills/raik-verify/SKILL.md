---
name: raik-verify
description: Proves that a change works before anyone calls it done. Use after implementing tasks, before closing or shipping a change, when the user asks whether something works, or when a previous result may be stale. Runs three layers of evidence (static checks and unit tests, one committed end-to-end test per spec scenario at mobile and desktop sizes, and screenshots that are actually looked at), re-runs earlier suites for regression, and writes the evidence into the change's tasks.
---

# raik-verify

Evidence or it did not happen. A green test proves what it asserts; a screenshot shows what nobody thought to assert. Use both.

## When to use

- After `raik-build`, before `raik-review` and `raik-ship`.
- Whenever someone is about to say "done", "fixed" or "it works".
- After any code change that follows an earlier verification (that evidence is now stale).

## Steps

### 1. Static checks and unit tests

Run `commands.static`, `commands.unit` and `commands.build` from the raik config (or the project's documented commands). Record each command and its result line ("19 passed", "0 errors"). A failure stops here: fix it or go to `raik-debug`.

### 2. End-to-end: one test per scenario

For each scenario in the change's spec, there must be a committed `@playwright/test` test that asserts it. Write missing ones. Details and patterns: `references/e2e.md`.

- Run at the configured viewports (default 360×800 and 1440×1000).
- In every test, also assert: no console errors, no uncaught exceptions, no horizontal scroll.
- States the fixtures never reach (empty, negative, error, limit) are forced, for example by intercepting a request or a module, never by editing shared fixtures.
- Then run the **whole** e2e suite: earlier changes are the regression.

Tests live in the repo and run in CI. A script in a temporary or ignored folder is not regression.

### 3. Look at it

With Playwright CLI (`playwright-cli`), or the e2e run's screenshots, capture each new or changed state at both viewports. **Open every screenshot and look.** Checklist in `references/screenshots.md`. Typical finds that tests miss: feedback rendered off-screen, impossible options offered, lines escaping a chart, text truncated on small screens.

Fix material problems, re-run steps 1 and 2, and take at most one more round of screenshots.

### 4. Write the evidence

Append to each task in `tasks.md` an `Evidence:` note with the commands run, counts, and anything found and fixed. In the change's status line, record the date and the limits of the evidence (for example "emulated Chromium, no physical devices").

### 5. Clean up

Stop what you started. When you stop a dev server, make sure the server process itself is gone (the port is free), not only the shell that launched it. Before killing a process, confirm it belongs to this project.

## Gates

- G3: every result you report comes from a command run after the last code change, in this session. If you edit code after verifying, verify again.
- A task is checked only with evidence. A failing check is reported with its output, never summarized as "mostly passing".

## Excuses

| Excuse | Rebuttal |
|---|---|
| "All tests pass, no need to look at screenshots." | Tests assert what you imagined. Screenshots show what you did not. |
| "I verified before the last small fix." | The fix invalidated it. Run it again. |
| "The old scripts still pass, regression is fine." | Only if they are committed and run in CI. Scripts in an ignored folder protect nothing. |
| "This state is hard to reach, I'll skip it." | Force it with interception. Hard-to-reach states are where bugs hide. |
| "It works on desktop." | Run the mobile viewport too; layout bugs live there. |
| "The server is stopped, I closed the terminal." | Check the port. Orphan servers break the next run. |

## Output

A short report: each layer with its commands and results, what the screenshots showed and what was fixed, the limits of the evidence, and the updated `tasks.md`.
