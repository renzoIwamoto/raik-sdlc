# External skills and tools

raik owns the workflow. For a job that an existing tool or skill does best, raik calls it instead of rewriting it. It never installs another end-to-end workflow collection: two skills that both define "how to plan" or "how to do TDD" make the agent pick at random.

## Tools (programs the skills run)

| Tool | Used by | Install | Notes |
|---|---|---|---|
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | `raik-change`, `raik-ship` | `npm install -g @fission-ai/openspec` | Global install; the project pins the expected version in its config. `openspec update` refreshes its agent instructions |
| [Playwright CLI](https://playwright.dev/agent-cli/skills) | `raik-verify`, `raik-ui` | `npm install -g @playwright/cli` | Exploratory checks and screenshots. Cheaper in tokens than the Playwright MCP server |
| `@playwright/test` | `raik-verify` | project dev dependency | Committed e2e tests and regression in CI |
| Test runners, linters, type checkers | `raik-build`, `raik-verify` | per stack | pytest, ruff, pyright, import-linter; Vitest, the project's linter, tsc |
| Terraform | `raik-ops` | per project | Infrastructure as code |

## Skills (used when installed)

| Skill | Used by | Why |
|---|---|---|
| Impeccable (pbakaus) | `raik-design`, `raik-ui` | Visual direction, critique and polish |
| Web Design Guidelines (vercel-labs/agent-skills) | `raik-ui` | Pre-ship audit of interface rules: accessibility, focus, forms, states |
| shadcn (official) | `raik-ui` | Correct use of shadcn/ui components, when the project uses them |
| Playwright CLI skill (`playwright-cli install --skills`) | `raik-verify` | Command reference for the CLI |

When a listed skill is missing, the raik skill still works and says what it skipped.

## Not used, on purpose

| Collection | Why not |
|---|---|
| obra/superpowers | A complete workflow of its own; it would compete with raik's. Two ideas are borrowed: hypothesis-driven debugging and verification before completion |
| addyosmani/agent-skills | Same reason. Two ideas are borrowed: excuse-and-rebuttal tables and review personas |
| Anthropic frontend-design, UI UX Pro Max | A second style engine next to Impeccable |
