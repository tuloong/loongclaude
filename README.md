# chung-agent-swarm

A minimal, runnable “Agent Swarm / Router–Worker” skeleton: Router/Coder/Reviewer/Tester specialists collaborate via a shared handoff protocol.

## Quickstart

## Run with Claude Code (recommended)

This repo includes Claude Code project subagents and skills:
- Subagents: `.claude/agents/` (swarm-router / swarm-coder / swarm-reviewer / swarm-tester)
- Workflow skill: `.claude/skills/swarm/` (invoke with `/swarm`)

In Claude Code:
1) Run `/swarm` and start with swarm-router to break down the task and produce a handoff JSON
2) Based on `next_role`, delegate to the matching subagent (or let Claude delegate automatically)
3) Iterate Coder → Reviewer → Tester until Reviewer outputs final LGTM

### Available skills

Run `/workflow-index` in Claude Code to see the full, up-to-date list. Common entry points:
- `/swarm`: generic Router → Coder → Reviewer → Tester loop
- `/feature`: requirements → design → implement → review → test
- `/bugfix`: triage → reproduce → fix → review → verify
- `/tdd`: red → green → refactor
- `/simplify`: eliminate redundancy and simplify control flow (behavior-preserving)
- `/review`: structured review (optional security pass)
- `/security`: security-focused review + remediation loop
- `/perf`: measure → optimize → re-measure
- `/docs`: update documentation to match behavior
- `/release`: release notes + checklist (no publishing)
- `/triage`: incident triage playbook

### Available subagents

Core roles:
- swarm-router, swarm-coder, swarm-reviewer, swarm-tester

Specialists:
- swarm-product, swarm-architect, swarm-debugger, swarm-refactorer
- swarm-security-reviewer, swarm-performance-optimizer, swarm-docs-writer
- swarm-release-manager, swarm-incident-triage, swarm-dependency-upgrader

### 1) Install

```bash
python -m pip install -e ".[dev]"
```

To enable the real Claude Agent SDK mode (optional):

```bash
python -m pip install -e ".[dev,agent_sdk]"
```

### 2) Run demo (offline, no external API calls)

```bash
python -m chung_agent_swarm demo
```

### 3) Run real mode (requires API key and SDK)

Set environment variable:

```bash
setx ANTHROPIC_API_KEY "YOUR_KEY"
```

Run:

```bash
python -m chung_agent_swarm run "Analyze this repository and propose improvements."
```

## Structure

- `CLAUDE.md`: Swarm global rules (role boundaries, handoff format)
- `.claude/docs/claud_platform_menu.md`: primary doc-first menu (Claude Platform + Claude Code links)
- `.claude/session_config.json`: per-session pre-flight notes (JSON schema + context window requirements)
- `swarm_docs.md`: implementation notes and extension guidance
- `src/chung_agent_swarm/`: core code
  - `protocol.py`: handoff protocol and shared state
  - `agents/`: Router/Coder/Reviewer/Tester
  - `orchestrator.py`: orchestration loop

## Handoff protocol

Each handoff must include a JSON object in output:

```json
{
  "type": "handoff",
  "next_role": "Reviewer",
  "summary": "Progress summary",
  "next_instructions": "Actionable tasks for the next agent"
}
```

## Development

Run tests:

```bash
python -m pytest
```

# loongclaude
