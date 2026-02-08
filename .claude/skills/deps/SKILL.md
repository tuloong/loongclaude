---
name: deps
description: Dependency upgrade workflow using swarm-dependency-upgrader with review and verification.
disable-model-invocation: true
---

Upgrade dependencies safely.

## Steps

1) Plan (swarm-router)
- Use `swarm-router` to define upgrade scope, constraints, and risk tolerance.

2) Upgrade (swarm-dependency-upgrader)
- Delegate to `swarm-dependency-upgrader`.
- Require: minimal-step upgrade plan, changes applied, and test results.

3) Review + verify (swarm-reviewer → swarm-tester)
- Reviewer checks for risk, config correctness, and dependency pinning rationale.
- Tester runs the full suite and reports results.
