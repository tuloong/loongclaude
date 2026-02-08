---
name: design
description: Design workflow (requirements → architecture → execution plan) using swarm-product and swarm-architect.
disable-model-invocation: true
---

Run a design-first workflow without implementing code yet.

## Steps

1) Requirements (swarm-product)
- Delegate to `swarm-product` to produce an acceptance checklist and edge cases.

2) Architecture (swarm-architect)
- Delegate to `swarm-architect` to propose a design, interfaces, invariants, and migration plan.

3) Execution plan (swarm-router)
- Delegate to `swarm-router` to turn the design into an actionable plan and choose the next specialist.
