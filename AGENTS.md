# AGENTS.md

Context for any coding agent working on raik-sdlc itself. Projects that *use* raik configure it in their own `AGENTS.md`; see `docs/configuration.md`.

## What this repo is

A set of Agent Skills (`skills/<name>/SKILL.md`) that encode one software delivery workflow, plus human docs (`docs/`). Only `skills/` is installed into projects; anything a skill needs at runtime must live inside its own folder.

## Rules for skills

1. **One folder per skill.** `name` in the frontmatter equals the folder name: lowercase letters, digits and hyphens, at most 64 characters. `description` says what the skill does *and when to use it*, at most 1024 characters.
2. **English, imperative, short.** Keep `SKILL.md` under ~400 lines. Move detail into `references/` and load it only when a step needs it.
3. **Same sections in every skill:** When to use, Steps, Gates (what must be true before moving on), Excuses (rationalizations and the rebuttal), Output.
4. **Grounded in practice.** A skill encodes something done and checked in a real project. What has not been piloted yet is marked in `docs/roadmap.md`, and the first pilot corrects the skill.
5. **Own words.** Ideas from other projects are credited in the README; text is never copied. No content from any employer.
6. **Tools over prose.** If a check can be a script (`scripts/`, Python stdlib), make it a script and have the skill run it.
7. **Agent-agnostic.** No instructions that only one agent can follow. Agent-specific extras are optional and say so.

## Before committing

```bash
python scripts/validate.py            # frontmatter, names, links
python -m unittest discover -s tests  # script tests
```

Conventional commits in English (`feat:`, `fix:`, `docs:`...). Update `CHANGELOG.md` under `Unreleased`.

## Layout

```
skills/<name>/SKILL.md      the skill
skills/<name>/references/   detail loaded on demand
skills/<name>/assets/       templates
skills/<name>/scripts/      runnable checks
docs/                       for humans: architecture, configuration, standards, ADRs
scripts/ tests/             repo tooling and its tests
.claude-plugin/             Claude Code plugin and marketplace manifests
```
