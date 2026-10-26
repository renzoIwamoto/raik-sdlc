# ADR 0002: OpenSpec for change specifications

- Status: Accepted
- Date: 2026-10-26

## Context

Every non-trivial change needs a proposal, a design, verifiable scenarios and tasks, and its spec must be merged into the living specs when it ships. OpenSpec does this and was used successfully on the project raik comes from. Friction seen there: it was run through `npm exec` with a pinned version (verbose and slow), and archiving moves a change into a dated folder, which breaks relative links.

## Decision

Use OpenSpec as the change layer, installed globally (`npm install -g @fission-ai/openspec`). The project pins the expected version in its raik config and `raik-change` reports a mismatch. `raik-ship` runs a script after `openspec archive` to repair links.

## Consequences

- One external tool to install; raik does not reimplement spec merging.
- Version drift between machines is detected, not prevented.
- If OpenSpec stops fitting, a native format can replace it behind the same skills.
