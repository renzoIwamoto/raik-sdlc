# AGENTS.md

Context for any coding agent working in this repository. Read it fully before proposing changes.

## What this project is

<One paragraph: the product, its users, its scope today and what it is not.>

## Where things are

| You need | Read |
|---|---|
| What the product is and is not | `docs/vision.md`, `PRODUCT.md` |
| User stories (`US-NN`) | `docs/product/user-stories.md` |
| Glossary and domain rules | `docs/domain.md` |
| Architecture, data, NFRs, security | `docs/architecture.md`, `docs/data-model.md`, `docs/nfr.md`, `docs/security.md` |
| Why something was decided | `docs/adr/` |
| Design system | `DESIGN.md` |
| Plan and status | `docs/roadmap.md` |
| Changes and specs | `openspec/` |

If anything here or in a conversation contradicts these files, the files win. If two files contradict each other, point it out before continuing.

## Stack

<Backend, frontend, data, hosting, infrastructure, with the raik profile names.>

## Non-negotiable rules

<From the chosen profiles, numbered. Example: dependencies point inward and are checked in CI; money is Decimal with explicit currency; no secrets or personal data in code, tests or logs.>

## Commands

```bash
# <component>
<install, test, lint, types, build, e2e>
```

## How we work

- Every non-trivial change goes through a proposal and spec before code (OpenSpec).
- Architecture decisions are new ADRs; accepted ADRs are not edited.
- Branches: <gitflow or trunk, as configured>. Never commit directly to `main`.
- Conventional commits in <code_language>, imperative.
- Docs and user-facing text in <docs_language>; code, identifiers and commits in <code_language>.

## raik

```yaml
raik:
  version: <x.y.z>
  docs_language: <es|en|...>
  code_language: en
  mode: ai-implements
  learnings: true
  stack:
    backend: python-fastapi-modular
    frontend: react-vite-ts
  changes:
    tool: openspec
    version: <x.y.z>
  git:
    branch_model: gitflow
    commit_style: conventional
    push: ask
  commands:
    unit: []
    static: []
    build: []
    e2e: []
  verify:
    viewports: [360x800, 1440x1000]
  design:
    skills: [impeccable, web-design-guidelines]
  memory:
    vault: ""
```
