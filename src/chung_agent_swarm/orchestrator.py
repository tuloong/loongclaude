from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .agents import CoderAgent, ReviewerAgent, RouterAgent, TesterAgent
from .protocol import AgentRole, SwarmState, TurnRecord, parse_handoff_from_text


DEFAULT_GLOBAL_RULES = """\
# Swarm Global Rules

## Role boundaries
- Router: routing and decomposition only, no code edits
- Coder: code changes and implementation only
- Reviewer: review and recommendations only, no code edits
- Tester: testing and verification only, no large refactors

## Handoff format
Each handoff must include a JSON object in the output:
{
  "type": "handoff",
  "next_role": "Reviewer|Coder|Tester|Router",
  "summary": "...",
  "next_instructions": "..."
}
"""


def load_global_rules(repo_root: Path) -> str:
    path = repo_root / "CLAUDE.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return DEFAULT_GLOBAL_RULES


@dataclass
class SwarmOrchestrator:
    state: SwarmState
    repo_root: Path

    def __post_init__(self) -> None:
        self.global_rules = load_global_rules(self.repo_root)
        self.agents = {
            AgentRole.ROUTER: RouterAgent(),
            AgentRole.CODER: CoderAgent(),
            AgentRole.REVIEWER: ReviewerAgent(),
            AgentRole.TESTER: TesterAgent(),
        }

    def is_done(self) -> bool:
        last = self.state.last_turn()
        if last is None:
            return False
        if last.role != AgentRole.REVIEWER:
            return False
        if "LGTM" not in last.output:
            return False
        return any(t.role == AgentRole.TESTER for t in self.state.turns)

    def step(self, user_input: str) -> str:
        agent = self.agents[self.state.current_role]
        result = agent.run(user_input=user_input, state=self.state)
        handoff = result.handoff or parse_handoff_from_text(result.text)
        record = TurnRecord(
            role=agent.role,
            input=user_input,
            output=result.text,
            handoff=handoff,
        )
        self.state.add_turn(record)
        return result.text


def run_demo(goal: str) -> int:
    repo_root = Path.cwd()
    state = SwarmState(goal=goal, current_role=AgentRole.ROUTER)
    orchestrator = SwarmOrchestrator(state=state, repo_root=repo_root)

    user_input = f"Goal: {goal}"
    for _ in range(8):
        output = orchestrator.step(user_input=user_input)
        print(f"\n[{state.turns[-1].role.value} OUTPUT]\n{output}\n")
        user_input = "Continue from the previous step."
        if orchestrator.is_done():
            break

    if orchestrator.is_done():
        print("Swarm demo finished: LGTM")
        return 0

    print("Swarm demo finished: reached max steps without LGTM")
    return 1


def run_real(prompt: str, max_turns: int) -> int:
    from .config import load_runtime_config

    cfg = load_runtime_config()
    if not cfg.anthropic_api_key:
        print("Missing ANTHROPIC_API_KEY. Set it in your environment to run real mode.")
        return 2

    try:
        from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
        from claude_agent_sdk.types import AssistantMessage
    except Exception as exc:
        print("Claude Agent SDK is not available. Install it, then retry.")
        print(f"Import error: {exc}")
        return 2

    import asyncio

    async def _main() -> int:
        options = ClaudeAgentOptions(
            max_turns=max_turns,
            allowed_tools=["Read", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch"],
        )

        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    text = getattr(block, "text", None)
                    if text:
                        print(text)
            elif isinstance(message, ResultMessage):
                print(f"Done: {message.subtype}")
                return 0

        return 0

    return asyncio.run(_main())
