---
name: raik
description: Entry point and orchestrator of the raik-sdlc workflow. Use for any software delivery request in a project whose AGENTS.md has a "## raik" section, or when the user says "raik", asks where the project stands or what is next, or wants to plan, decide, specify, build, debug, verify, review, ship, document or deploy something. Reads project state, routes to the right raik-* skill and enforces the workflow gates, so the user never has to remember which skill to call.
---

# raik

The user says what they want in plain words. You work out the stage, run the right skill, and keep the gates. The user should never need to know a skill name.

## When to use

- Any request about building or changing the product: features, fixes, docs, decisions, infrastructure, releases.
- `raik status` (where are we), `raik next` (what comes next), `raik decide-for-me` (take my recommendations for the open questions).
- At the start of a session in a raik project, to re-establish context.

## Steps

### 1. Load the configuration

Read the `## raik` section of `AGENTS.md` (a YAML block; every key optional). Note `docs_language`, `mode`, `stack`, `commands`, `git` and `changes`. Talk to the user in `docs_language`; write code, commits and identifiers in `code_language`.

If there is no `## raik` section, say so in one line and offer `raik-init`. Do not invent the configuration.

### 2. Read the project state

Collect only what is needed for the request, in this order:

1. `docs/roadmap.md` (or the roadmap path): current phase and its checkpoint.
2. Active changes: `openspec list` (OpenSpec projects). A change with all tasks done but not archived is unfinished work.
3. `git status -sb` and the current branch: uncommitted work, commits not pushed.
4. The latest session note or evidence, if the project keeps them.

### 3. Classify the request

| The user wants to... | Stage | Skill |
|---|---|---|
| Start a project, or adopt raik in an existing repo | init | `raik-init` |
| Describe the product, users, voice, user stories | product | `raik-product` |
| Name things, define business rules, find edge cases | domain | `raik-domain` |
| Choose stack or structure; data, API, security, NFRs, operations; write an ADR | architecture | `raik-architecture` |
| Set the visual direction or the design system | design | `raik-design` |
| Build or improve a screen | ui | `raik-ui` |
| Plan phases, check whether a phase can close | roadmap | `raik-roadmap` |
| Settle open questions or trade-offs | decide | `raik-decide` |
| Add or change behavior (not trivial) | change | `raik-change` |
| Implement agreed tasks | build | `raik-build` |
| Understand an unexpected failure or a bug | debug | `raik-debug` |
| Prove it works | verify | `raik-verify` |
| Review a diff for errors, simplicity, security | review | `raik-review` |
| Close a change, commit, open a PR, release | ship | `raik-ship` |
| Infrastructure, pipelines, environments, deploys, monitoring | ops | `raik-ops` |
| Save continuity, record learnings | memory | `raik-memory` |

A request can span stages. Run them in this order and stop at each gate: decide, change, build, verify, review, ship.

If the request is ambiguous between two stages, pick the earlier one; never skip forward past a gate.

### 4. Announce and run

Say in one line which skill you are using and why, in `docs_language`. Example: "Using raik-change: this adds behavior, so it needs a spec before code." Then follow that skill.

If the skill is not installed, say so, do the step following the project's `AGENTS.md` and docs, and keep every gate.

### 5. Close the turn

End with: what was done, the evidence (commands and results), what is pending, and the next step. In `ai-implements` mode with `learnings: true`, add two or three learnings tied to what was just done.

## Gates

Stop and say which gate blocks the flow when one is not met.

| Gate | Rule |
|---|---|
| G1 Decisions | Product and architecture choices belong to the user. Recommend, then wait for an answer or an explicit "decide for me"; afterwards list what you chose. Record each decision where it belongs (`raik-decide`). |
| G2 Change first | No build without an agreed change. Exempt: typos, version bumps, styling with no behavior change. |
| G3 Evidence | Nothing is "done", "fixed" or "passing" without output from commands you ran after the last code change, in this session. Report failures with their output. |
| G4 Authorization | No commit, push, PR, deploy, publish or deletion of shared resources without the user's go-ahead for that batch. Approval for one batch does not cover the next. |
| G5 Docs travel with code | Docs, specs and roadmap change in the same change as the behavior they describe. |

## Commands

- **`raik status`**: phase and checkpoint, active changes with task counts, uncommitted or unpushed work, open gaps of the phase. Five lines or a short table.
- **`raik next`**: the single most valuable next step and why; offer at most one alternative.
- **`raik decide-for-me`**: for the open questions of the current round, take your recommendations, apply them and list each one in one line.

## Modes

- `ai-implements` (default): you implement; the user decides and reviews. Explain decisions briefly.
- `user-implements`: you guide. Propose the failing test, let the user write the code, review with hints before solutions. You may do mechanical work (config, commands, docs) when asked.
- `pair`: ask per task who writes it.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "It is a small feature, a spec is overkill." | If it changes behavior, write the change; it takes minutes and becomes the test plan. Only typos, versions and styling are exempt. |
| "The tests passed earlier." | Earlier is not evidence. Run them again after the last edit. |
| "The user approved a push before." | Approval covers one batch. Ask again. |
| "I'll update the docs at the end." | The end never comes. Update them in the same change. |
| "I know which option they want." | Then recommend it and let them confirm. Choosing for them without saying so breaks G1. |
| "Status needs the whole repo read." | Read only what the request needs, in the order above. |

## Output

A one-line routing announcement, the stage skill's output, and a closing summary with evidence, pending items and the next step.
