from __future__ import annotations

from dataclasses import dataclass

from ..protocol import AgentResult, AgentRole, HandoffEnvelope, SwarmState, format_handoff
from .base import SwarmAgent


@dataclass(frozen=True)
class ReviewerAgent(SwarmAgent):
    def __init__(self) -> None:
        super().__init__(
            role=AgentRole.REVIEWER,
            instructions=(
                "You are the Reviewer agent. You audit security and correctness. "
                "You must not edit files; only report issues and recommended fixes. "
                "If acceptable, output 'LGTM' and hand off to Tester or Router."
            ),
        )

    def run(self, user_input: str, state: SwarmState) -> AgentResult:
        text = "LGTM (demo mode) No real audit performed."
        handoff = HandoffEnvelope(
            next_role=AgentRole.TESTER,
            summary="Reviewer approved in demo mode.",
            next_instructions="In demo mode, provide placeholder test results.",
        )
        return AgentResult(text=f"{text}\n\n{format_handoff(handoff)}", handoff=handoff)
