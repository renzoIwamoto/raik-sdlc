# Standards

The base engineering standards raik applies. Each separates what is **required** (checked, not negotiable without an ADR) from what is **flexible** (a default the project can change).

The standards live inside the skills that apply them, because only `skills/` is installed in a project. This page is the index.

| Standard | Summary | Source |
|---|---|---|
| Backend `python-fastapi-modular` | Modular monolith by business capability; ports and adapters inside each module; boundaries checked by import-linter (tested contracts); same use cases for every entrypoint; `Decimal` money | [profile](../skills/raik-architecture/references/profile-python-fastapi-modular.md) |
| Frontend `react-vite-ts` | TypeScript strict; tokens as the only source of style; required screen states; WCAG AA by script; generated API client; Vitest and committed Playwright e2e | [profile](../skills/raik-architecture/references/profile-react-vite-ts.md) |
| Architecture concerns | Every concern of a professional app decided or marked N/A: structure, data, interfaces, security, quality numbers, operations, product-facing, AI | [checklist](../skills/raik-architecture/references/concerns.md) |
| Design system | What `DESIGN.md` contains: direction, tokens by role, type, spacing, components and states, motion, data visualization, accessibility | [reference](../skills/raik-design/references/design-system.md) |
| Screen states | Loading, empty, partial, error, limit, offline, success, access revoked; control states; number formatting | [reference](../skills/raik-ui/references/screen-states.md) |
| Infrastructure | Terraform with remote state, pinned versions, separate environments, least privilege, workload identity federation, no console changes | [reference](../skills/raik-ops/references/infrastructure.md) |
| Pipelines | Checks and plan on pull requests, one artifact promoted from dev to prod with approval | [reference](../skills/raik-ops/references/pipelines.md) |
| Testing | Test first for rules; one e2e per spec scenario at two viewports; forced edge states; screenshots reviewed | [e2e](../skills/raik-verify/references/e2e.md), [screenshots](../skills/raik-verify/references/screenshots.md) |
| Review | Correctness, tests, security and simplicity checklists | [checklists](../skills/raik-review/references/checklists.md) |
| Changes | Proposal, design, spec and tasks templates | [artifacts](../skills/raik-change/references/artifacts.md) |
