---
name: simplify
description: Code simplification workflow (identify → simplify → verify) using swarm-simplifier with review and testing.
disable-model-invocation: true
---

Run a behavior-preserving code simplification workflow.

## Steps

1) Scope (swarm-router)
- Use `swarm-router` to define what must remain equivalent (behavior, interfaces, invariants).

2) Simplify (swarm-simplifier)
- Delegate to `swarm-simplifier`.
- Require: DRY/KISS refactors only, better naming, reduced branching, and utility consolidation where appropriate.

3) Review + verify (swarm-reviewer → swarm-tester)
- Reviewer focuses on behavioral equivalence, readability, layering, and any performance tradeoffs.
- Tester runs the relevant suite and/or targeted repro steps.
