---
name: perf
description: Performance workflow (measure → optimize → re-measure) using swarm-performance-optimizer.
disable-model-invocation: true
---

Run a performance optimization loop.

## Steps

1) Define the metric (swarm-router)
- Use `swarm-router` to define the target metric and acceptable regression thresholds.

2) Optimize (swarm-performance-optimizer)
- Delegate to `swarm-performance-optimizer`.
- Require: baseline measurement, change summary, and post-change measurement.

3) Review + verify (swarm-reviewer → swarm-tester)
- Reviewer checks correctness and maintainability of the optimization.
- Tester runs relevant tests and reports results.
