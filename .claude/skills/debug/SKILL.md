---
name: debug
description: Debug workflow (repro → isolate → fix → verify) using swarm-debugger with review and testing.
disable-model-invocation: true
---

Run a debugging workflow.

## Steps

1) Route (swarm-router)
- Use `swarm-router` to define expected behavior and a minimal reproduction plan.

2) Debug and fix (swarm-debugger)
- Delegate to `swarm-debugger`.
- Require: exact repro commands, root cause evidence, smallest safe fix, and verification results.

3) Review (swarm-reviewer)
- Delegate to `swarm-reviewer` for correctness and maintainability review.

4) Verify (swarm-tester)
- Delegate to `swarm-tester` to run tests and report results.
