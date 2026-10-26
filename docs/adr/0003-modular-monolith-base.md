# ADR 0003: Modular monolith as the backend base standard

- Status: Accepted
- Date: 2026-10-26

## Context

The author wants backends that are well structured by business area, flexible, and still held to a common standard. Microservices cost a solo developer or a small team a lot (network calls, contract versions, distributed tracing) before they pay off. A layered monolith (`domain/`, `use_cases/`, `adapters/` at the top) is cheap at first but lets unrelated features couple over time.

## Decision

The default backend profile is a modular monolith: modules by business capability, ports and adapters inside each module, boundaries checked in CI, one image deployed by role. A small app is one module. A module becomes a separate service only for a measured reason, recorded in an ADR. Details in [standards](../standards.md).

## Consequences

- Each business area can be understood, tested and changed alone.
- Module boundaries must be designed and enforced (import-linter contracts).
- Extracting a service later is a move, not a rewrite.
