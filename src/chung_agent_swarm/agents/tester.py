from __future__ import annotations

from dataclasses import dataclass

from ..protocol import AgentResult, AgentRole, HandoffEnvelope, SwarmState, format_handoff
from .base import SwarmAgent


@dataclass(frozen=True)
class TesterAgent(SwarmAgent):
    def __init__(self) -> None:
        super().__init__(
            role=AgentRole.TESTER,
            instructions=(
                "You are the Tester agent. You design/run tests and summarize failures with repro steps. "
                "You must not do large refactors."
            ),
        )

    def run(self, user_input: str, state: SwarmState) -> AgentResult:
        text = "(demo mode) pytest: 1 passed, 0 failed"
        handoff = HandoffEnvelope(
            next_role=AgentRole.REVIEWER,
            summary="Tester passed in demo mode.",
            next_instructions="Provide the final sign-off.",
        )
        return AgentResult(text=f"{text}\n\n{format_handoff(handoff)}", handoff=handoff)
