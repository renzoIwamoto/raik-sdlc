# Change artifacts

Templates for the four files of a change. Write the prose in the project's `docs_language`; keep OpenSpec headings and SHALL/MUST in English.

## proposal.md

```markdown
# Proposal

Status: proposed, not implemented. Decisions taken with <user> on <date>. Scope: <what part of the system>.

## Why

<The user stories, domain rules or roadmap gap this serves, with links. What is missing today, observed in the code or docs.>

## What Changes

- <Observable change, one per line.>

## Capabilities

### New Capabilities

- `<capability>`: <one line>.

### Modified Capabilities

<List, or "None".>

## Impact

Expected files: <paths>. Verification: <unit, e2e, screenshots>.

Out of scope: <explicit list>.
```

Update the status line as the change moves: proposed → implemented and verified on <date> → archived on <date>.

## design.md

```markdown
# Design

## Context

<What the code does today, precisely. Constraints.>

## Goals / Non-Goals

**Goals:** ...
**Non-Goals:** ...

## Decisions

1. **<Decision>.** <What and why. Alternatives rejected and why.>

## Risks / Trade-offs

- [<Risk>] → <mitigation>.

## Migration Plan

<Order of work, data changes, rollback.>
```

When implementation reveals that a decision must change, update it here with the reason ("Adjusted during implementation: ...").

## specs/<capability>/spec.md

```markdown
# Spec Delta

## Purpose

<What this capability covers and what it does not promise.>

## ADDED Requirements

### Requirement: <name>
<The system> SHALL <behavior>.

#### Scenario: <name>
- **WHEN** <action or state>
- **THEN** <observable result>
```

Use `MODIFIED`, `REMOVED` or `RENAMED` sections for existing capabilities. A good scenario names concrete values ("a S/ 100 purchase in September and a S/ 40 refund in October") so the test writes itself.

## tasks.md

```markdown
# Tasks

Status: not started. <Who implements, per mode.>

## 1. <Group>

- [ ] 1.1 <What to change>. Verify: <command or check>.
```

`raik-verify` appends `Evidence: <what ran and the result>` to each task when it passes. `raik-ship` refuses to archive a change with a checked task that has no evidence.
