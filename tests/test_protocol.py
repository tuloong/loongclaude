from chung_agent_swarm.protocol import (
    AgentRole,
    HandoffEnvelope,
    SwarmState,
    TurnRecord,
    format_handoff,
    parse_handoff_from_text,
)


def test_format_and_parse_handoff_roundtrip() -> None:
    handoff = HandoffEnvelope(
        next_role=AgentRole.REVIEWER,
        summary="ok",
        next_instructions="review it",
    )
    text = f"hello\n\n{format_handoff(handoff)}\n"
    parsed = parse_handoff_from_text(text)
    assert parsed == handoff


def test_swarm_state_updates_current_role_on_handoff() -> None:
    state = SwarmState(goal="x", current_role=AgentRole.ROUTER)
    handoff = HandoffEnvelope(
        next_role=AgentRole.CODER,
        summary="go",
        next_instructions="do",
    )
    state.add_turn(
        TurnRecord(role=AgentRole.ROUTER, input="i", output="o", handoff=handoff)
    )
    assert state.current_role == AgentRole.CODER
