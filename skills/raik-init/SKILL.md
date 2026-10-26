---
name: raik-init
description: Sets up a repository to work with raik-sdlc. Use when starting a new project, when adopting raik in an existing repo, or when a project has no "## raik" section in AGENTS.md. Writes AGENTS.md with the project summary, rules and the raik configuration, creates the docs and roadmap skeleton, initializes OpenSpec, sets the branch model and quality gates for the chosen stack profile, and lists the external tools and skills to install. In an existing repo it maps what exists instead of restructuring it.
---

# raik-init

Give every agent the same starting context and the same rules, in one file every agent reads.

## When to use

- A new repository.
- An existing repository adopting raik.
- `raik` found no `## raik` section.

## Steps

### 1. Look before writing

Inventory what exists: `AGENTS.md`, `CLAUDE.md` or other agent files, `README.md`, `docs/`, ADRs, `openspec/`, stack files (`pyproject.toml`, `package.json`, `infra/`), CI workflows, branches. In an existing repo, **map, do not restructure**: point the config at what is there and propose migrations as roadmap items.

### 2. Ask the setup round

Through `raik-decide`, one round: product name and one-line description; `docs_language`; working `mode`; stack profiles (backend, frontend) or "decide later"; branch model; push policy; whether to use an external notes vault. Recommend defaults; accept "decide for me".

### 3. Write AGENTS.md

From `assets/agents-template.md`: what the project is, where each thing lives, the stack, the non-negotiable rules (from the chosen profiles), commands, how the team works, and the `## raik` YAML block (see the repo's `docs/configuration.md` for keys). If `AGENTS.md` exists, add the missing sections and the `## raik` block; keep the existing content.

For agents that read their own file (for example `CLAUDE.md`), create it with a pointer to `AGENTS.md` plus only agent-specific notes, so rules live in one place.

### 4. Create the skeleton

Only what the next steps fill: `docs/roadmap.md` (from the `raik-roadmap` template, Phase 0 "Foundations"), `docs/adr/` with ADR 0001 recording the adoption of raik and the stack profile, and an index of the docs that `raik-product`, `raik-domain` and `raik-architecture` will write. Empty documents are not created ahead of time.

### 5. Tools and quality gates

- OpenSpec: check `openspec --version`; if missing, show `npm install -g @fission-ai/openspec`; then `openspec init` (after confirming) and record the version in the config.
- Playwright CLI for browser checks: `npm install -g @playwright/cli`.
- Optional design skills per `design.skills`: show their install commands.
- For the chosen profiles, set up the gates the profile requires (formatter, linter, strict types, tests, boundary contracts) and a first CI workflow via `raik-ops`. In an existing repo, add only what is missing and say what you added.
- `.gitattributes` with `* text=auto eol=lf` and a `.gitignore` for the stack.

### 6. Branches

With gitflow: create `develop` from `main` if missing; work continues on `feature/*`. Creating or pushing branches follows gate G4.

### 7. Report

What was created or changed, what was mapped as-is, tools to install, and the next step (usually `raik-product`).

## Gates

- G1: setup choices are the user's (defaults offered).
- G4: no push, remote branch or repository setting changed without authorization.
- Never overwrite an existing file wholesale; merge into it.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "Faster to regenerate AGENTS.md from scratch." | It holds decisions someone made. Merge; do not overwrite. |
| "Create every doc now so the structure is complete." | Empty docs look finished and are not. Create them when they get content. |
| "Restructure the repo to match the profile while we're here." | That is a change with risk. Propose it on the roadmap; do it through `raik-change`. |

## Output

`AGENTS.md` with the `## raik` block, the roadmap and ADR 0001, the quality gates added, the tools to install, and the next step.
