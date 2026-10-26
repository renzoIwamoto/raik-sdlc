# ADR 0001: Agent Skills format and distribution

- Status: Accepted
- Date: 2026-10-26

## Context

raik must work with any coding agent the author uses (Claude Code and Codex today) and be installable by others.

## Decision

Write every skill in the open [Agent Skills](https://agentskills.io/) format: one folder with a `SKILL.md` (frontmatter `name` and `description`) plus optional `references/`, `assets/` and `scripts/`. Distribute through the `skills` CLI (`npx skills add renzoIwamoto/raik-sdlc`) and, for Claude Code, a plugin manifest in `.claude-plugin/`. No custom installer.

## Consequences

- One source works in every compatible agent.
- Only `skills/` is installed; runtime material cannot live in `docs/`.
- Agent-specific features (slash commands, subagents) can only be optional extras.
