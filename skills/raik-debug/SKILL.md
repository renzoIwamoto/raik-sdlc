---
name: raik-debug
description: Finds the root cause of a failure with hypotheses and evidence instead of guesses. Use when a test fails unexpectedly, a bug is reported, behavior differs from the spec, a command or build breaks, or two attempted fixes have not worked. Reproduces the failure, ranks hypotheses with the evidence each predicts, tests one at a time, fixes at the root with a regression test, and stops to report after three failed attempts.
---

# raik-debug

Debugging is an experiment, not a guessing game. Every change you make should be designed to prove or disprove one idea.

## When to use

- An unexpected test, build, lint or runtime failure.
- A bug report or a mismatch between behavior and spec.
- After two fixes that did not work: stop and switch to this process.

## Steps

### 1. Reproduce

Get the smallest exact reproduction: the command, input and environment that fail every time. Read the **whole** error, including the first lines of the stack trace and any earlier warning. If it does not reproduce, that is the first finding: record the conditions and look for what differs.

### 2. Hypothesize

Write two or three hypotheses. For each, say what evidence would confirm or rule it out. Rank them by likelihood and by how cheap the test is.

### 3. Test one at a time

Run the cheapest decisive test first: read the code path, add a log or assertion, check a value, bisect the history (`git bisect`) or the input. Change one thing per experiment and record the result. Revert experimental edits that did not help.

### 4. Find the root cause

Keep asking "why" until you reach a cause that, if fixed, makes the failure impossible rather than unlikely. Then check every caller and every place with the same pattern: the root is often shared.

### 5. Fix with a regression test

Write a test that fails for the root cause; fix it at the shared point; see the test pass; run the related suites. The fix is the smallest change that removes the cause.

### 6. Record

In the change or the commit message: the symptom, the root cause, the fix, and the test that now guards it.

## Stop rule

After three failed hypotheses or fixes, stop. Report to the user what you tried, what you learned, the remaining hypotheses and what you need (access, data, a decision). Do not keep changing code at random.

## Gates

- Never weaken, skip or delete a test to make it pass without the user's agreement and a recorded reason.
- G3: "fixed" requires the regression test and the related suites passing after the fix.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "I'll try a few things and see." | Random changes hide the cause and add new bugs. One hypothesis at a time. |
| "The error message is long, the last line is enough." | The first lines and earlier warnings usually name the cause. Read all of it. |
| "It's flaky, re-run until green." | Flaky is a bug with a timing or ordering cause. Find it. |
| "The test is wrong, I'll relax it." | Maybe. Prove it against the spec and ask before changing it. |
| "Fixed in the place it was reported." | Check the other callers. The same root breaks them too. |

## Output

The reproduction, the hypotheses tested with results, the root cause, the fix with its regression test, and the suites run.
