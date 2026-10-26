---
name: raik-domain
description: Builds the domain model in words before it becomes code. Use when naming business concepts, writing or changing business rules, finding edge cases, resolving terminology that differs between docs, code and conversation, or preparing fixtures. Produces a glossary with the exact code name of every term, numbered domain rules that each map to a test, and a list of edge cases to cover.
---

# raik-domain

The domain document is the contract between the business and the code. If a rule is not written here, the code is guessing.

## When to use

- After `raik-product`, before architecture details and before any domain code.
- When a conversation, doc and code use different words for one thing, or one word for two things.
- When a change adds or alters a business rule.

## Steps

### 1. Collect the language

From the stories, the conversation and existing code, list every business term. Note synonyms and collisions.

### 2. Write the glossary

`docs/domain.md`, a table: term in `docs_language` | meaning | **name in code** (`code_language`, usually English). One term, one meaning, one code name. Enum values are listed too (`expense`, `refund`...). Code uses the code names; documents use the terms.

Keep `CONTEXT.md` as a short plain-language summary of the vocabulary for people who will not read the rules.

### 3. Write the rules

Numbered, one rule per item, each testable:

```
7. **Deduplication:** <rule in one or two sentences, with the decision when the case is ambiguous>.
```

- Numbers are stable. New rules are appended; changed rules keep their number and note the date of the change.
- Every rule names what happens in the ambiguous case (usually: hold for the user, never guess silently).
- Money, dates, time zones and currencies get explicit rules (precision, rounding, which date counts).
- Each rule maps to at least one test named after it when the code exists.

### 4. List the edge cases

A section "Edge cases to cover with fixtures": real-world variants the rules must survive (formats, duplicates, partial data, reversals). They become fixtures and tests in `raik-build`.

### 5. Check consistency

Rules against stories and data model; glossary against code identifiers. Report every mismatch; propose the fix; let the user choose when it changes behavior.

## Gates

- G1: business rules are decisions. Recommend, then record what the user approved, with the date.
- No domain code for a concept that has no glossary entry and code name.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "The code is the documentation." | The code shows what it does, not what it should do. Rules are the should. |
| "Edge cases are rare." | Rare cases are where money and trust are lost. List them. |
| "Spanish names in code are clearer for us." | Mixed-language identifiers multiply ambiguity. Map each term to one code name. |
| "I'll renumber the rules to keep them grouped." | Tests, commits and docs cite the numbers. Append, never renumber. |

## Output

`docs/domain.md` (glossary, numbered rules, edge cases), `CONTEXT.md`, and the list of mismatches found with proposed fixes.
