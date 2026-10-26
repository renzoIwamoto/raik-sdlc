# Configuration

A project opts into raik with a `## raik` section in its `AGENTS.md`. Every agent reads `AGENTS.md` at the start of a session, so the configuration reaches all of them without another file.

The section holds one YAML block. Every key is optional; missing keys take the default shown.

## Example

````markdown
## raik

```yaml
raik:
  version: 0.1.0                 # raik-sdlc version this project follows
  docs_language: es              # language of docs and messages to the user
  code_language: en              # identifiers, commits, comments
  mode: ai-implements            # ai-implements | user-implements | pair
  learnings: true                # close each delivery with 2-3 learnings

  stack:
    backend: python-fastapi-modular   # see docs/standards.md
    frontend: react-vite-ts

  changes:
    tool: openspec
    version: 1.14.1                   # checked against `openspec --version`

  git:
    branch_model: gitflow        # gitflow | trunk
    commit_style: conventional
    push: ask                    # ask | never | allowed

  commands:                      # run from the repo root
    unit: ["cd backend && uv run pytest", "cd web && pnpm test"]
    static: ["cd backend && uv run ruff check . && uv run pyright && uv run lint-imports", "cd web && pnpm lint"]
    build: ["cd web && pnpm build"]
    e2e: ["cd web && pnpm e2e"]
    dev_server: "cd web && pnpm dev --host 127.0.0.1 --port 5173 --strictPort"

  verify:
    viewports: [360x800, 1440x1000]
    screenshots: true

  design:
    skills: [impeccable, web-design-guidelines]

  memory:
    vault: ""                    # optional path to an external notes vault
```
````

## Keys

| Key | Default | Meaning |
|---|---|---|
| `version` | latest installed | raik-sdlc version the project follows |
| `docs_language` | `en` | Language for documents and for talking to the user |
| `code_language` | `en` | Language for code, identifiers, commits and comments |
| `mode` | `ai-implements` | Who writes code. `ai-implements`: the agent implements and the user decides. `user-implements`: the agent guides, proposes the failing test and reviews. `pair`: the agent asks per task |
| `learnings` | `true` | Close each delivery with two or three concrete learnings |
| `stack.backend` | none | Backend profile from [standards](standards.md) |
| `stack.frontend` | none | Frontend profile from [standards](standards.md) |
| `changes.tool` | `openspec` | Change specification tool |
| `changes.version` | none | Expected tool version; a mismatch is reported, not fatal |
| `git.branch_model` | `gitflow` | `gitflow`: `feature/*` from `develop`, `release/*` and `hotfix/*` to `main`. `trunk`: short branches to `main` |
| `git.commit_style` | `conventional` | Commit message convention |
| `git.push` | `ask` | `ask`: authorization per batch (gate G4). `never`: the user pushes. `allowed`: push after verification |
| `commands.*` | none | Commands the skills run. Without them, the skills look for the project's documented commands and ask if unsure |
| `verify.viewports` | `[360x800, 1440x1000]` | Viewports for e2e and screenshots |
| `verify.screenshots` | `true` | Whether screenshots are taken and reviewed |
| `design.skills` | `[]` | Design skills to use when installed |
| `memory.vault` | empty | Optional notes vault for cross-session continuity |
