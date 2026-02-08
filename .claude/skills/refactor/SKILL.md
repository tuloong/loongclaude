---
name: refactor
description: Refactoring workflow (identify → refactor → verify) using swarm-refactorer with review and testing.
disable-model-invocation: true
---

Run a safe refactoring workflow.

## Steps

1) Scope (swarm-router)
- Use `swarm-router` to define what must stay the same (behavior and interfaces).

2) Refactor (swarm-refactorer)
- Delegate to `swarm-refactorer`.
- Require: incremental changes, tests stay green, and a before/after summary.

3) Review + verify (swarm-reviewer → swarm-tester)
- Reviewer focuses on readability, layering, and risk.
- Tester runs the full suite.
