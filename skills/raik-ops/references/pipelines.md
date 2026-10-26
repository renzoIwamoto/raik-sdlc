# Pipelines (GitHub Actions)

Adapt names and commands to the project's raik config (`commands`). Pin actions to a major version or a commit SHA.

## Pull request: checks

```yaml
name: CI
on:
  pull_request:
  push:
    branches: [develop, main]
permissions:
  contents: read

jobs:
  backend:
    runs-on: ubuntu-latest
    defaults: { run: { working-directory: backend } }
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: uv sync --locked
      - run: uv run ruff check . && uv run ruff format --check .
      - run: uv run pyright
      - run: uv run lint-imports
      - run: uv run pytest
      - run: uv run pip-audit

  web:
    runs-on: ubuntu-latest
    defaults: { run: { working-directory: web } }
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm, cache-dependency-path: web/pnpm-lock.yaml }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm build
      - run: pnpm test
      - run: pnpm exec playwright install --with-deps chromium
      - run: pnpm e2e

  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: gitleaks/gitleaks-action@v2
        env: { GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}" }
```

Add Dependabot (`.github/dependabot.yml`) for each package ecosystem and for GitHub Actions.

## Terraform plan on pull requests

```yaml
  terraform-plan:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    permissions: { contents: read, id-token: write, pull-requests: write }
    defaults: { run: { working-directory: infra/envs/dev } }
    steps:
      - uses: actions/checkout@v4
      - uses: google-github-actions/auth@v2      # or the provider's OIDC action
        with:
          workload_identity_provider: ${{ vars.WIF_PROVIDER }}
          service_account: ${{ vars.TF_PLAN_SA }}
      - uses: hashicorp/setup-terraform@v3
      - run: terraform fmt -check -recursive ../../
      - run: terraform init -input=false
      - run: terraform validate
      - run: terraform plan -input=false -no-color -out=tfplan
```

Post the plan summary to the pull request so the reviewer reads it there.

## Deploy

```yaml
name: Deploy
on:
  push:
    branches: [develop]       # dev
    tags: ["v*.*.*"]          # prod
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ startsWith(github.ref, 'refs/tags/') && 'prod' || 'dev' }}   # prod requires approval in repo settings
    permissions: { contents: read, id-token: write }
    steps:
      - uses: actions/checkout@v4
      - uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ vars.WIF_PROVIDER }}
          service_account: ${{ vars.DEPLOY_SA }}
      # Build the image once, push it, then apply Terraform and deploy that exact image digest.
```

Use GitHub environments with required reviewers for `prod`, so the approval gate is enforced by the platform, not by convention.
