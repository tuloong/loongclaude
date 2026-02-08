from __future__ import annotations

from dataclasses import dataclass

from ..protocol import AgentResult, AgentRole, HandoffEnvelope, SwarmState
from .base import SwarmAgent


@dataclass(frozen=True)
class RouterAgent(SwarmAgent):
    def __init__(self) -> None:
        super().__init__(
            role=AgentRole.ROUTER,
            instructions=(
                "You are the Router agent. Choose the next specialist based on the goal and latest progress. "
                "You must not write code; only route and decompose tasks."
            ),
        )

    def run(self, user_input: str, state: SwarmState) -> AgentResult:
        last = state.last_turn()
        if last is None:
            return AgentResult(
                text="Goal received. Handing off to Coder to propose an executable implementation and file changes.",
                handoff=HandoffEnvelope(
                    next_role=AgentRole.CODER,
                    summary="Router initialized the workflow.",
                    next_instructions=f"Goal: {state.goal}\nProduce an implementation skeleton and key file contents.",
                ),
            )

        if last.role == AgentRole.CODER:
            return AgentResult(
                text="Handing off to Reviewer for security and correctness review.",
                handoff=HandoffEnvelope(
                    next_role=AgentRole.REVIEWER,
                    summary="Coder produced an implementation.",
                    next_instructions="Review the previous output, identify risks/defects, and decide whether it passes.",
                ),
            )

        if last.role == AgentRole.REVIEWER:
            return AgentResult(
                text="Handing off to Tester to run verification and report results.",
                handoff=HandoffEnvelope(
                    next_role=AgentRole.TESTER,
                    summary="Reviewer completed review.",
                    next_instructions="Run/design tests, then summarize results and reproducible steps.",
                ),
            )

        if last.role == AgentRole.TESTER:
            return AgentResult(
                text="Testing completed. Handing back to Reviewer for final sign-off.",
                handoff=HandoffEnvelope(
                    next_role=AgentRole.REVIEWER,
                    summary="Tester provided verification results.",
                    next_instructions="Based on test results, provide final conclusion: LGTM or a fix list.",
                ),
            )

        return AgentResult(text="Unable to determine next step; defaulting to Coder.", handoff=HandoffEnvelope(
            next_role=AgentRole.CODER,
            summary="Router fallback routing.",
            next_instructions=f"Goal: {state.goal}\nContinue making progress.",
        ))
