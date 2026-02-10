---
name: workflow-index
description: Index of available project subagents and skills for common engineering workflows.
disable-model-invocation: true
---

List the available project subagents and skills in this repository, and recommend which to use for a given task.

## Subagents (project-level)
- swarm-router: routes and decomposes tasks (read-only)
- swarm-coder: implements code changes (edits allowed)
- swarm-reviewer: reviews changes (no edits)
- swarm-tester: runs/tests verification (no edits)
- swarm-product: clarifies requirements and acceptance criteria (read-only)
- swarm-architect: proposes designs and migration plans (read-only)
- swarm-debugger: reproduces and fixes failures (edits allowed)
- swarm-refactorer: behavior-preserving refactors (edits allowed)
- swarm-simplifier: DRY/KISS code simplifications without behavior change (edits allowed)
- swarm-security-reviewer: security-focused review (no edits)
- swarm-performance-optimizer: measure-driven performance work (edits allowed)
- swarm-docs-writer: updates docs to match behavior (edits allowed)
- swarm-release-manager: release notes and checklist (read-only)
- swarm-incident-triage: incident triage and mitigations (may run commands)
- swarm-dependency-upgrader: safe dependency upgrades (edits allowed)
- swarm-git-worktree-manager: parallel git workflows using worktrees (may run commands)

## Skills (slash commands)
- /swarm: generic Router → Coder → Reviewer → Tester loop
- /feature: product → architect → swarm loop
- /bugfix: triage → debugger → review → verify
- /tdd: red → green → refactor
- /review: structured review (optional security pass)
- /security: security review + remediation
- /perf: measure → optimize → re-measure
- /docs: update documentation
- /release: release notes + checklist
- /triage: incident triage playbook
- /debug: repro → fix → verify
- /refactor: behavior-preserving refactors
- /simplify: eliminate redundancy and simplify control flow (behavior-preserving)
- /deps: safe dependency upgrades
- /design: requirements → architecture → execution plan

## Usage
Pick a skill that matches your intent, or explicitly ask Claude Code to use a specific subagent (e.g., “Use swarm-debugger to fix failing tests”). If you are unsure, start with swarm-router.
