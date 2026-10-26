---
name: raik-memory
description: Keeps continuity across sessions and turns work into learning. Use at the end of a delivery or session, when the user changes how they want to work, when resuming after a break, or when the user asks to remember or record something. Saves a short session note (task, changes, evidence, blockers, next step), durable preferences and decisions in the right place, two or three concrete learnings, and, if configured, entries in the user's external notes vault following that vault's own rules.
---

# raik-memory

The next session should start where this one ended, without re-reading everything or repeating mistakes.

## When to use

- After `raik-ship`, or when a session ends with work in progress.
- When the user states a lasting preference ("from now on...", "remember that...").
- At the start of a session, to resume (read before writing).

## Steps

### 1. Resume (start of session)

Read the latest session note and the roadmap's last progress entry. Check they are still true against the repo (`git status`, `openspec list`); notes describe the past, the repo is the present.

### 2. Decide where each thing belongs

| What | Where |
|---|---|
| Product, domain, architecture or design decisions | The project docs (`raik-decide` table) |
| Progress and evidence of a change | The roadmap and the change's tasks |
| How the user wants the agent to work | The agent's memory if it has one, and `AGENTS.md` when it applies to every agent |
| Task in progress, blockers, next step | A session note |
| Facts about the user across projects | The external vault, if `memory.vault` is set |

Do not duplicate: the repo is the source of truth for anything about the code.

### 3. Write the session note

Short bullets: goal and constraints; what changed (paths, commits); evidence actually run; blockers; the **next concrete step**; branch or PR. Mark a note closed when its work is done.

### 4. External vault (optional)

If `memory.vault` points to a notes vault, read its own rules first (for example its `AGENTS.md`) and follow them: where new entries go, file naming, frontmatter, what must not be stored. Default to its inbox; do not rewrite its main notes unless the user asks. Never commit or sync the vault automatically.

### 5. Learnings

In `ai-implements` mode with `learnings: true`, close the delivery with two or three learnings tied to what just happened: why a technique worked, a mistake that was caught and how, a tool behavior worth knowing. Concrete, one or two sentences each, no tutorials.

## Rules

- Never store secrets, tokens, passwords, account or card numbers, or health data.
- Store facts and decisions, not guesses; mark proposals as pending until the user adopts them.
- Date every entry; when a fact replaces another, say "now X (before Y)".

## Excuses

| Excuse | Rebuttal |
|---|---|
| "I'll remember next time." | The next session starts empty. Write the next step down. |
| "Put everything in the note to be safe." | Notes that duplicate the repo go stale. Link to the source instead. |
| "The vault is just notes, I can reorganize it." | It has its own rules and owner. Follow them; add, don't rewrite. |

## Output

The session note, any preference or decision recorded where it belongs, vault entries if configured, and the learnings.
