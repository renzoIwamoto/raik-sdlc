---
name: raik-architecture
description: Defines the complete architecture of a professional application. Use when choosing the stack or structure, designing data, APIs, security, quality targets or operations, writing or superseding an ADR, or checking that no architectural concern was left undecided. Applies a stack profile (modular monolith with ports and adapters for Python backends, strict React and TypeScript for web) and walks a checklist where every concern is decided or explicitly marked not applicable.
---

# raik-architecture

Architecture is the set of decisions that are expensive to change. Make them on purpose, write them down, and leave none to accident.

## When to use

- Starting a product, after `raik-product` and `raik-domain`.
- A change that touches structure: a new container, module, integration, data store or security boundary.
- Reviewing whether the architecture is complete before a phase closes.
- Replacing a decision: write a new ADR that supersedes the old one.

## Steps

### 1. Read the inputs

Vision, user stories, domain rules, non-functional expectations already stated, and existing ADRs. Read the code if it exists; describe what is there, not what the docs wish.

### 2. Choose the stack profile

Load the profile for each part of the system:
- Backend: `references/profile-python-fastapi-modular.md` (modular monolith, ports and adapters, boundaries in CI).
- Web: `references/profile-react-vite-ts.md`.

A project may deviate from a profile's flexible items freely and from a required item only with an ADR that says why. Record the chosen profiles in the raik config (`stack`).

### 3. Walk every concern

Go through `references/concerns.md` group by group: structure, data, interfaces, security and privacy, quality attributes with numbers, operations, product-facing. For each concern, write the decision or "N/A: <reason>". Open choices go to `raik-decide` as a round; do not decide product-relevant trade-offs alone.

### 4. Write the documents

| Document | Contents |
|---|---|
| `docs/architecture.md` | Style and dependency rule; C4 levels 1 to 3 in Mermaid; the module map; sequence diagrams for flows that cross containers or handle failure; deployment; open questions |
| `docs/data-model.md` | Entities and relations (Mermaid ER), ownership per module, money and time types, authorization per table with its test |
| `docs/nfr.md` | Targets with numbers: latency p95, availability SLO, limits, cost budget, retention |
| `docs/security.md` | Data classification, threat model, secrets, logging rules, compliance |
| `docs/adr/NNNN-<slug>.md` | One per significant decision, from `assets/adr-template.md` |

Diagrams are Mermaid in Markdown, so they live in the repo and change with the code.

### 5. ADR rules

- One decision per ADR, numbered in order, never renumbered.
- An **accepted** ADR is never edited. To change it, write a new ADR with `Supersedes: ADR NNNN` and mark the old one `Superseded by ADR MMMM` (the only edit allowed).
- Context states facts with sources; Decision is checkable against the code; Consequences include what now must be monitored.

### 6. Make it enforceable

Turn rules into checks where possible: import-linter contracts for boundaries, a test per authorization policy, CI jobs for audits. A rule nobody checks erodes; list the ones that remain manual.

## Gates

- G1: architecture choices with product impact (cost, privacy, vendor lock-in, scope) are the user's. Recommend; let them decide.
- No concern left blank: decided, N/A with reason, or listed as an open question with the phase that will decide it.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "We will think about security later." | Later the data model and auth are fixed. Threat-model now, briefly. |
| "Microservices will scale better." | They cost before they pay. Start modular, extract with a measured reason. |
| "NFRs are obvious, no numbers needed." | Without numbers nobody can tell when they are broken. |
| "I'll just edit the old ADR." | Accepted ADRs are history. Supersede it. |
| "Observability is an ops detail." | Deciding what to log and measure shapes the code. Decide it here. |
| "This concern does not apply." | Then write "N/A" and why, so the next reader knows it was considered. |

## Output

Updated architecture documents and ADRs, the chosen profiles in the config, a list of open questions with the phase that decides them, and the checks that enforce the rules.
