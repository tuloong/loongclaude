# Claude Agent Swarm Guide v1.0

## 1. Definition

In a Claude Code / Agent SDK workflow, an Agent Swarm can be implemented as a network of specialized roles coordinated by an orchestrator and linked via a handoff protocol that preserves shared state.

Core capabilities:
- Handoffs: one specialist finishes a phase and hands control to the next
- Parallelization: multiple specialists can be queried in parallel for comparison/verification, then synthesized by Router (or an integrator)
- Shared state: all roles rely on the same core context and progress state (for example `CLAUDE.md` + `SwarmState`)

## 2. Reference implementation (this repository)

### 2.1 Architecture: Router–Worker
- Router: understands the goal, decomposes tasks, selects the next agent, defines acceptance criteria
- Workers:
  - Coder: implements changes
  - Reviewer: audits and suggests fixes
  - Tester: verifies with tests and repro steps

### 2.2 Key modules
- `src/chung_agent_swarm/protocol.py`
  - `AgentRole`: role enum
  - `SwarmState`: shared state (goal, turn history, artifacts)
  - `HandoffEnvelope`: handoff payload (next_role + summary + next_instructions)
- `src/chung_agent_swarm/orchestrator.py`
  - `SwarmOrchestrator`: main loop (route → execute → parse handoff → update state)
  - `run_demo()`: offline demo mode
  - `run_real()`: real SDK mode (requires ANTHROPIC_API_KEY + claude_agent_sdk)
- `src/chung_agent_swarm/agents/`
  - `router.py` `coder.py` `reviewer.py` `tester.py`

### 2.3 Running with Claude Code (project configuration)

This repo includes Claude Code project configuration for running the swarm directly:
- `.claude/agents/`: project subagents (YAML frontmatter + system prompt)
- `.claude/skills/swarm/`: the `/swarm` workflow skill (manual invocation)

## 3. Handoff protocol

Each handoff must include a JSON object:

```json
{
  "type": "handoff",
  "next_role": "Reviewer",
  "summary": "Progress summary",
  "next_instructions": "Actionable tasks for the next agent"
}
```

Recommended constraints:
- `summary` must include: done, todo, risks/blockers
- `next_instructions` must be actionable (not just “continue”)

## 4. Parallelization guidance

Phase 1 (logical parallelism):
- Router dispatches read-only analysis tasks to multiple specialists (e.g., Reviewer + Tester + Architect) and synthesizes the results.

Phase 2 (code parallelism):
- Use Git worktrees/branches to isolate code-changing work
- Use an integrator role to merge and run a unified test suite

## 5. Testing guidance

Suggested scenario:
- From an empty directory, scaffold a FastAPI project with unit tests

Expected loop:
- Coder generates code → Tester runs tests → Reviewer outputs LGTM or a fix list → iterate until verified
