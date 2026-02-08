from __future__ import annotations

from dataclasses import dataclass

from ..protocol import AgentResult, AgentRole, SwarmState


@dataclass(frozen=True)
class SwarmAgent:
    role: AgentRole
    instructions: str

    def run(self, user_input: str, state: SwarmState) -> AgentResult:
        raise NotImplementedError
