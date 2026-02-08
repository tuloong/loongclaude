from chung_agent_swarm.agents.router import RouterAgent
from chung_agent_swarm.protocol import AgentRole, SwarmState, TurnRecord


def test_router_initial_routes_to_coder() -> None:
    agent = RouterAgent()
    state = SwarmState(goal="goal", current_role=AgentRole.ROUTER)
    result = agent.run(user_input="x", state=state)
    assert result.handoff is not None
    assert result.handoff.next_role == AgentRole.CODER


def test_router_after_coder_routes_to_reviewer() -> None:
    agent = RouterAgent()
    state = SwarmState(goal="goal", current_role=AgentRole.ROUTER)
    state.add_turn(TurnRecord(role=AgentRole.CODER, input="i", output="o", handoff=None))
    result = agent.run(user_input="x", state=state)
    assert result.handoff is not None
    assert result.handoff.next_role == AgentRole.REVIEWER
