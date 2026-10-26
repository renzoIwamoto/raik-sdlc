# Roadmap

**Current version:** 0.1.0 (first release candidate, 2026-10-26). Author: Renzo Iwamoto.

## Origin

raik-sdlc encodes the workflow used to build Cuentelia (a closed-source expense tracker, 2026-10). The practices in each skill were done and checked there first: decision rounds, OpenSpec changes, three-layer verification with screenshot review, archive with link repair, phase-close reviews.

## Status of the skills

| Skill | Piloted on a real project | Notes |
|---|---|---|
| `raik`, `raik-decide`, `raik-change`, `raik-verify`, `raik-ship` | Yes (Cuentelia) | `archive_links.py` dry-run clean on Cuentelia's four archived changes |
| `raik-product`, `raik-domain`, `raik-architecture`, `raik-design`, `raik-ui`, `raik-roadmap` | Yes (Cuentelia phase 0) | Modular import-linter contracts tested on a sample package; `contrast.py` run on Cuentelia's tokens |
| `raik-build`, `raik-debug`, `raik-review`, `raik-memory` | Partly | Practices used in Cuentelia; not yet run as explicit skills |
| `raik-init` | No | First pilot: adopt raik in Cuentelia |
| `raik-ops` | Partly | CI used in Cuentelia; Terraform pilot in Cuentelia phase 2 |

## Next

1. **Publish 0.1.0**: push, then check installation with `npx skills add renzoIwamoto/raik-sdlc` (Claude Code and Codex) and as a Claude Code plugin; tag `v0.1.0` when both work.
2. **Pilot in Cuentelia**: run `raik-init` to add the `## raik` section; close the remaining phase 0 gaps through `raik`; record what each skill got wrong and fix it here.
3. **Trigger checks**: test that each description makes the agent load the right skill and not the others (for example with Anthropic's skill-creator evals).
4. **0.2.0, AI pack**: `raik-llm` (prompts, structured output, evals, cost, privacy; pilot: Cuentelia's LLM fallback), `raik-mcp` (tools, OAuth, same use cases; pilot: Cuentelia phase 6), `raik-agents`, `raik-rag`. From public knowledge only.
5. **More profiles** when a project needs them (for example a TypeScript backend or a mobile app).

## Decisions

See [ADRs](adr/): Agent Skills format (0001), OpenSpec for changes (0002), modular monolith as backend base (0003).
