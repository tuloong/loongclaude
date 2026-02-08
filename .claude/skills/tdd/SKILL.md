---
name: tdd
description: TDD workflow (red → green → refactor) using project subagents.
disable-model-invocation: true
---

Run a test-driven development loop.

## Steps

1) Plan the tests (swarm-router)
- Use `swarm-router` to define the smallest testable unit and acceptance criteria.

2) Write failing tests (swarm-coder)
- Delegate to `swarm-coder` to add minimal failing tests first.
- Require: clear test names and minimal fixtures.

3) Implement (swarm-coder)
- Continue with `swarm-coder` to implement the minimal code to make tests pass.

4) Refactor (swarm-refactorer)
- Delegate to `swarm-refactorer` to improve structure while preserving behavior.
- Require: test suite stays green.

5) Review + verify (swarm-reviewer → swarm-tester)
- Reviewer checks correctness and maintainability.
- Tester runs the full suite and reports results.
