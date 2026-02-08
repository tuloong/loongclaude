from __future__ import annotations

from chung_agent_swarm.session_config import SESSION_CONFIG_TEMPLATE, validate_session_config


def test_session_config_template_is_valid() -> None:
    result = validate_session_config(SESSION_CONFIG_TEMPLATE)
    assert result.ok
