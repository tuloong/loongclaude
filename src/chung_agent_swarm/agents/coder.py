from __future__ import annotations

from dataclasses import dataclass

from ..protocol import AgentResult, AgentRole, HandoffEnvelope, SwarmState, format_handoff
from .base import SwarmAgent


@dataclass(frozen=True)
class CoderAgent(SwarmAgent):
    def __init__(self) -> None:
        super().__init__(
            role=AgentRole.CODER,
            instructions=(
                "You are the Coder agent. You implement code and edit files. "
                "When done, you must output a handoff JSON for Reviewer."
            ),
        )

    def run(self, user_input: str, state: SwarmState) -> AgentResult:
        text = (
            f"Goal received: {state.goal}\n"
            "(demo mode) This is where key files would be created/edited with a change summary."
        )
        handoff = HandoffEnvelope(
            next_role=AgentRole.REVIEWER,
            summary="Coder produced placeholder output in demo mode.",
            next_instructions="Review whether the placeholder output follows role boundaries and the handoff protocol.",
        )
        return AgentResult(text=f"{text}\n\n{format_handoff(handoff)}", handoff=handoff)
