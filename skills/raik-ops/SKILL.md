---
name: raik-ops
description: Sets up and changes infrastructure, pipelines, environments, releases and monitoring. Use when creating or modifying cloud resources, writing or fixing CI/CD, adding an environment, deploying, preparing a release, or adding logs, metrics and alerts. Uses Terraform by default with remote state and no manual console changes, CI authenticated by workload identity federation, checks and plan on every pull request, and apply or deploy only after approval.
---

# raik-ops

Infrastructure is code, pipelines are the only way to production, and nothing changes in a console by hand.

## When to use

- Creating the first environment, or adding services, databases, queues, keys or DNS.
- Writing or changing CI/CD pipelines.
- Releasing, deploying or rolling back.
- Adding observability: structured logs, metrics, traces, alerts, uptime checks.

## Steps

### 1. Read the decisions

`docs/architecture.md` (containers, deployment, environments), `docs/nfr.md` (SLOs, budget), `docs/security.md` (secrets, data) and the infrastructure ADRs. If a needed decision is missing (region, provider, environments), run `raik-decide` or `raik-architecture` first.

### 2. Infrastructure with Terraform

Layout and rules in `references/infrastructure.md`:
- `infra/modules/<name>` for reusable pieces, `infra/envs/<env>` for each environment, remote state with locking, providers and modules pinned.
- One service account per workload with least privilege; secrets in a secret manager, referenced, never in `.tfvars` committed.
- `terraform fmt -check`, `terraform validate` and `terraform plan` before any apply. Read the plan; summarize additions, changes and **destructions** for the user.

### 3. Pipelines

Templates in `references/pipelines.md`:
- **Pull request:** lint, types, unit tests, boundary checks, build, e2e, dependency and secret scans, `terraform plan` (posted to the PR).
- **Merge to the integration branch or tag:** build the image once, deploy to dev; promote the same artifact to prod with an approval.
- CI authenticates to the cloud with workload identity federation; no long-lived keys in secrets.

### 4. Releases

Semantic versions; `CHANGELOG.md`; with gitflow, `release/<version>` merged to `main` and `develop`, tagged on `main`. A rollback is a redeploy of the previous tag, documented and tried at least once.

### 5. Observability

- Structured logs (JSON) with request ids; never bodies with personal data, tokens or full account numbers.
- Metrics for the SLOs in `docs/nfr.md`; an alert when an SLO burns, not on every error.
- Uptime check on public endpoints; a runbook entry for each alert.

## Gates

- G4: `terraform apply`, deploys to any shared environment and releases happen only with the user's go-ahead after they have seen the plan or the release notes.
- No manual console changes; a hotfix made by hand is imported into Terraform the same day.
- A plan with destructions is called out explicitly before approval.

## Excuses

| Excuse | Rebuttal |
|---|---|
| "Faster to click it in the console." | Then the next apply reverts it or fails. Write it in Terraform. |
| "A service account key in CI secrets is simpler." | Keys leak and do not expire. Use workload identity federation. |
| "The plan is long, apply and see." | Read it. One destroyed database is enough. |
| "We'll add monitoring after launch." | Then the first outage is reported by users. Add the SLO metrics with the service. |
| "Deploy straight from my machine this once." | Deploys come from the pipeline, so they are repeatable and audited. |

## Output

Terraform changes with the reviewed plan summary, pipeline files, release notes or deploy results, observability added, and what still needs the user's approval.
