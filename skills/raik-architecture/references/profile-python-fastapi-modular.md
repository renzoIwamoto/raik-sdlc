# Profile: python-fastapi-modular

Backend base standard. A **modular monolith**: one codebase and one image, split by business capability, with ports and adapters inside each module. Deployed by role (for example a public `api` and a private worker), not by module.

## Layout

```
src/<package>/
  modules/
    <capability>/            e.g. transactions, ingestion, billing
      domain/                models and rules; no I/O
      application/           use cases; the module's public API
      ports/                 Protocols the module needs (repositories, gateways, clock)
      adapters/              implementations: persistence, HTTP clients, queues
  shared/                    kernel used by every module: money, time, errors, ids
  entrypoints/               FastAPI routers, MCP server, workers; thin, call application/
tests/
  <capability>/              unit tests for domain and application
  integration/               adapters against real services or containers
```

A small app is one module. Add modules when a business capability changes independently.

## Required

1. Dependencies point inward: `entrypoints → application → domain`; `adapters` implement `ports`. Domain code has no I/O and imports nothing from adapters, frameworks or clients.
2. A module never imports another module's internals. It calls the other module's `application` API, or reacts to its events.
3. Every entrypoint (web API, MCP, workers, CLI) calls the same use cases. No business logic in an entrypoint.
4. Boundaries are checked in CI with `import-linter` (contracts below).
5. Tooling: `uv` (`uv sync --locked`), `ruff` (with security rules `S`), `pyright` strict, `pytest`.
6. Configuration from environment variables (Pydantic settings); secrets never in the repo or in logs.
7. Money is `Decimal` with an explicit currency; never `float`, never sums across currencies.
8. Pydantic v2 models at the edges (requests, responses, external payloads); plain dataclasses or Pydantic in the domain, consistently.
9. Errors: domain errors are typed exceptions; entrypoints map them to HTTP problem responses (RFC 9457). No bare `except`.

## Flexible (default first)

- Persistence: plain SQL with `psycopg` 3, or SQLAlchemy Core. An ORM only with a reason in an ADR.
- Communication between modules: direct calls to `application`; in-process events when a module should not know the other.
- Extracting a module into its own service: only for a measured reason (scale, isolation, ownership), in an ADR.

## Drawing module boundaries

Group what changes together. Validate with the change test: a typical business change should touch one module. If most changes touch three, the boundaries are wrong. Name modules after business capabilities (`billing`), not technical layers (`services`).

## import-linter contracts

Tested with import-linter 2.15: the wildcards cover new modules without editing the config, and both an import between two modules' domains and a domain importing its own adapters break the build.

```toml
[tool.importlinter]
root_package = "<package>"
include_external_packages = true   # needed to forbid third-party packages

[[tool.importlinter.contracts]]
name = "Modules only meet through their application API"
type = "independence"
modules = ["<package>.modules.*"]
ignore_imports = ["<package>.modules.** -> <package>.modules.*.application"]

[[tool.importlinter.contracts]]
name = "Layers inside each module"
type = "layers"
containers = ["<package>.modules.*"]
layers = ["adapters", "application", "ports", "domain"]

[[tool.importlinter.contracts]]
name = "Domain and shared stay pure"
type = "forbidden"
source_modules = ["<package>.modules.*.domain", "<package>.shared"]
forbidden_modules = ["<package>.entrypoints", "fastapi", "httpx", "psycopg"]
```

A wildcard `*` cannot be followed by `**` in `ignore_imports`; write `modules.**`, not `modules.*.**`. The ignore lets any layer call another module's `application`; keep those calls in `application` or `adapters` and catch the rest in review.

## Tests

- Domain and application: fast unit tests with fakes for ports. Every domain rule has a test named after it.
- Adapters: integration tests against the real service or a container, marked so they can run separately.
- Entrypoints: a few API tests per route through FastAPI's test client.
