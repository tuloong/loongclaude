---
name: docs
description: Documentation workflow using swarm-docs-writer (update docs to match current behavior).
disable-model-invocation: true
---

Update documentation to match current code behavior.

## Steps

1) Identify doc gaps (swarm-router)
- Use `swarm-router` to list which docs need updates and what must be added/removed.

2) Write docs (swarm-docs-writer)
- Delegate to `swarm-docs-writer`.
- Require runnable commands and minimal examples.

3) Review (swarm-reviewer)
- Delegate to `swarm-reviewer` focusing on clarity and correctness.
