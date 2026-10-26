# Infrastructure standard (Terraform)

## Layout

```
infra/
  modules/
    <name>/            main.tf, variables.tf, outputs.tf, README.md
  envs/
    dev/               backend.tf, providers.tf, main.tf (calls modules), terraform.tfvars (no secrets)
    prod/
  bootstrap/           one-time: state bucket, CI identity federation (applied by hand once, documented)
```

## Required

1. Remote state with locking (for example a GCS bucket with versioning, or S3 with a lock table), one state per environment.
2. Terraform and provider versions pinned (`required_version`, `required_providers`); `.terraform.lock.hcl` committed.
3. Separate environments (`dev`, `prod`), ideally separate cloud projects or accounts.
4. One identity per workload with least privilege. Services that only encrypt get encrypt permission, not decrypt.
5. Secrets in the cloud secret manager; Terraform creates the secret resource, the value is set out of band or by a pipeline with access. Never in `.tfvars` or state outputs.
6. CI authenticates with workload identity federation (OIDC), scoped to the repository and branch.
7. `terraform fmt -check`, `validate` and `plan` in every pull request that touches `infra/`; `apply` only from the pipeline after approval.
8. Tags or labels on every resource: `app`, `env`, `managed-by=terraform`.
9. No manual console changes. Anything created by hand is imported (`terraform import` or `import` blocks) or deleted.

## Review a plan

Summarize for the user: resources to add, change and **destroy**; anything replaced (destroy then create); IAM changes; cost-relevant changes. Destructions of stateful resources (databases, buckets, keys) need explicit confirmation and a backup.
