# Review checklists

## Correctness

- Every spec scenario is handled; trace each one through the code.
- Boundary values: zero, negative, empty list, one item, maximum, missing optional field, duplicate.
- Errors: every call that can fail is handled or deliberately propagated; no swallowed exceptions; user sees an actionable message.
- Money and time: `Decimal` and explicit currency; no mixed currencies; time zones explicit; the right date (operation vs received) used.
- Concurrency and retries: idempotent where retried; no lost updates; cursors advanced only after durable writes.
- State: no stale data after edits; caches invalidated; UI reflects the saved state.
- Boundaries: no imports across module internals; entrypoints thin; business rules in the domain.

## Tests

- One test per scenario and per domain rule, named after it.
- The test would fail if the behavior broke (not only asserting that something renders).
- Edge states forced, not skipped; regression suites still run.
- No sleeping or timing assumptions; no reliance on test order.
- Fixtures anonymized; no real personal data.

## Security

- Input validated at the trust boundary (types, ranges, lengths, formats).
- Authorization checked on the server for every operation and every object (no IDOR); row-level policies tested.
- No secrets, tokens or personal data in code, logs, errors or client bundles.
- Queries parameterized; no string-built SQL, shell or HTML (injection, XSS).
- External calls have timeouts; responses are validated before use.
- Files and uploads: type and size limits; never executed or served from user paths.
- Dependencies: pinned, audited, from expected sources; new ones justified.
- AI features: untrusted text never becomes instructions or tool arguments without validation (prompt injection); data sent to providers matches consent.

## Simplicity

- Code that is not needed by any scenario.
- The same rule implemented twice.
- Abstractions with one implementation, configuration for values that never change.
- A dependency or helper the standard library or the platform already provides.
- Names that need a comment to be understood.
