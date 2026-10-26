---
name: raik-ship
description: Closes a verified change and delivers it. Use when a change's tasks are implemented and verified, or when the user asks to close, archive, commit, push, open a pull request or release. Checks that every task has fresh evidence, updates the docs and roadmap, archives the OpenSpec change syncing its spec and repairing links, splits the work into conventional commits, follows the branch model, and pushes or opens the PR only with the user's authorization.
---

# raik-ship

Shipping is where unfinished work gets disguised as finished. This skill refuses that.

## When to use

- After `raik-verify` (and `raik-review`) on a change.
- When the user says "close", "archive", "commit", "push", "PR" or "release".

## Steps

### 1. Preflight

1. Every checked task in `tasks.md` has an `Evidence:` note produced after the last code change. If not, run `raik-verify` first (gate G3).
2. `git status`: list what will be committed. Only files that belong to this change. Nothing generated, nothing local (screenshots in ignored folders stay out), no secrets. Run the project's secret scanner if it has one.
3. Run the static checks and tests one last time if anything changed since verification.

### 2. Update the documents

In the same change (gate G5): the change's status lines (proposal and tasks: "implemented and verified on <date>"), the roadmap and the phase review if the change closes a gap, and any design brief or doc the change made stale.

### 3. Commit the work

Conventional commits in `code_language`, imperative mood: `feat: show net spend on the dashboard`. Split by purpose so history reads well:
- dependency or tooling changes (`build:`),
- the behavior change with its tests and docs (`feat:` / `fix:`),
- the archive (`docs:`), in step 4.

Add the attribution lines your agent's instructions require. Never commit to `main` directly.

### 4. Archive the change

```bash
openspec archive <name> --yes
python <this skill>/scripts/archive_links.py <name>
```

- Never use `--skip-specs` for a change with behavior specs; it is only for tooling changes without specs.
- The script repairs relative links inside the archived folder and points references elsewhere at the dated archive path. Read its output; investigate any link it reports as broken.
- Set the archived proposal and tasks status to "archived on <date>". Commit: `docs: archive <name> and sync its spec`.

### 5. Branch, push and pull request

Follow `git.branch_model`:
- **gitflow**: work on `feature/<name>` from `develop`; PR to `develop`. Releases from `release/<version>`, urgent fixes from `hotfix/<name>`, both merged to `main` and `develop`.
- **trunk**: short-lived branch, PR to `main`.

Before any push or PR, show the user what will leave the machine (branch, commits, target) and wait for their go-ahead for this batch (gate G4), unless `git.push` is `allowed`. Pushes can be slow; run them in the background when your agent supports it and report when they finish. Confirm the remote state afterwards (`git status -sb` shows no ahead/behind).

### 6. Release (when asked)

Bump the version (semver), move `Unreleased` in `CHANGELOG.md` under the new version with the date, tag `vX.Y.Z`, and push the tag with authorization.

### 7. Hand over

Report the commits (hash and subject), what was archived and which spec it created or updated, the remote state, and the next step. In `ai-implements` mode with learnings on, add two or three learnings. Offer `raik-memory` if the session should be saved.

## Gates

- G3: no archive and no commit of a task without evidence.
- G4: no push, PR, tag or release without authorization for this batch.
- No direct commits to `main`.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "Verification was green an hour ago." | If code changed since, it is stale. Re-run. |
| "One big commit is simpler." | Split commits make review and revert possible. Feature, then archive. |
| "--skip-specs is faster." | It drops the behavior spec from the living specs. Only for tooling changes. |
| "Links will be fixed later." | Run the script now; it takes a second and later never comes. |
| "The user approved pushing yesterday." | Each batch needs its own go-ahead. |
| "Screenshots are evidence, commit them." | Keep evidence where the project keeps it; do not commit ignored or temporary files. |

## Output

Commits with hashes, the archive result, the remote state, pending items and the next step.
