# Best Practices (Claude Code)

Upstream:
- Best practices: https://code.claude.com/docs/en/best-practices

## Context is the limiting resource

The docs emphasize that the context window fills up fast (files read, command output, and long conversations), and quality can degrade as context fills.

Practical implications:
- Prefer scoped tasks, especially for investigations
- Use sub-agents for high-volume exploration to keep your main session focused
- Clear or compact between unrelated tasks

## Always give verification

Claude performs better when it can verify work:
- run tests
- run linters
- compare outputs
- reproduce bugs deterministically

## Explore → plan → code

Use plan mode for complex tasks so exploration and planning happen before edits.

## Keep CLAUDE.md concise

CLAUDE.md is loaded every session, so keep it short and focused on rules that Claude cannot infer from the repo (workflow constraints, build/test commands, non-obvious conventions).

## Use deterministic guardrails

When instructions are not enough, use hooks to enforce rules deterministically (format-on-write, block edits to protected paths, require tests before completion).
