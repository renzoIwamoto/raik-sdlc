# Architecture concerns

Walk every concern. For each, either record a decision (a section of the architecture docs or an ADR) or mark it "N/A" with one line of reason. A concern skipped silently is a decision made by accident.

Use the questions as prompts, not as a form to copy.

## 1. Structure

| Concern | Decide |
|---|---|
| Context (C4 level 1) | Who uses the system; which external systems it talks to and why |
| Containers (C4 level 2) | Deployable pieces, their technology, how they talk, what each may access |
| Components (C4 level 3) | Modules or layers inside each container; the dependency rule |
| Stack profile | Which profile from `references/profile-*.md`; deviations and why |
| Main flows | A sequence diagram for each flow that crosses containers or has failure handling |

## 2. Data

| Concern | Decide |
|---|---|
| Model | Entities, relations, ownership per module; money and time types |
| Migrations | Tool, forward-only or reversible, who runs them in each environment |
| Authorization at data level | Row-level security or per-query tenant filters; a test per table |
| Retention and deletion | What is kept, for how long, how a user's data is deleted |
| Backups and recovery | Frequency, restore tested, recovery point and time objectives |

## 3. Interfaces

| Concern | Decide |
|---|---|
| API style | REST with OpenAPI (default), GraphQL or RPC; naming |
| Errors | One format (RFC 9457 problem details); stable error codes |
| Versioning and compatibility | How breaking changes are introduced |
| Pagination, filtering, limits | Cursor or offset; maximum page size; rate limits |
| Idempotency | Which operations accept retries safely, and how (keys, natural ids) |
| Events and queues | Producers, consumers, delivery guarantees, retries, dead letters |
| External integrations | Timeouts, retries with backoff, circuit breaking, what happens when they are down |

## 4. Security and privacy

| Concern | Decide |
|---|---|
| Authentication | Provider, session or token type, lifetime, refresh |
| Authorization | Roles or ownership rules; where they are enforced (never only in the UI) |
| Threat model | Assets, entry points, top threats and mitigations (STRIDE as a checklist) |
| Secrets | Where they live, who can read them, rotation |
| Sensitive data | Classification, encryption at rest and in transit, masking in logs |
| Compliance | Applicable laws (data protection, consumer), consent records |
| Supply chain | Dependency pinning, audit in CI, secret scanning, update policy |

## 5. Quality attributes (with numbers)

| Concern | Decide |
|---|---|
| Performance | Latency targets per key operation (p95), payload limits |
| Availability | SLO per user-facing journey; what "down" means |
| Scalability | Expected load now and in a year; what scales and how |
| Cost | Monthly budget; the biggest cost drivers; alerts |
| Accessibility | WCAG level and how it is checked |

## 6. Operations

| Concern | Decide |
|---|---|
| Environments | dev, staging, prod; what differs; how data is seeded |
| Infrastructure as code | Tool (Terraform default), state, module layout |
| CI/CD | What runs on PR, on merge, on tag; who approves deploys |
| Release strategy | Versioning, release branches, rollbacks, feature flags |
| Observability | Structured logs (no personal data), metrics, traces, dashboards |
| Alerting and on-call | What pages someone, runbooks for the top failures |

## 7. Product-facing

| Concern | Decide |
|---|---|
| Internationalization | Languages, number, date and currency formats, time zones |
| Analytics | What is measured, consent, where it is stored |
| Notifications | Channels (email, push), preferences, unsubscribe |
| AI features (if any) | Model choice, evals and thresholds, cost per call, data sent to providers and consent, prompt injection defenses |
