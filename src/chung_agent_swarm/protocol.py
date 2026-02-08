from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
import json
import re
from typing import Any, Literal


class AgentRole(str, Enum):
    ROUTER = "Router"
    CODER = "Coder"
    REVIEWER = "Reviewer"
    TESTER = "Tester"


@dataclass(frozen=True)
class HandoffEnvelope:
    next_role: AgentRole
    summary: str
    next_instructions: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["next_role"] = self.next_role.value
        return data

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "HandoffEnvelope":
        return HandoffEnvelope(
            next_role=AgentRole(str(data["next_role"])),
            summary=str(data.get("summary", "")),
            next_instructions=str(data.get("next_instructions", "")),
        )


@dataclass(frozen=True)
class AgentResult:
    text: str
    handoff: HandoffEnvelope | None = None


@dataclass(frozen=True)
class TurnRecord:
    role: AgentRole
    input: str
    output: str
    handoff: HandoffEnvelope | None = None


@dataclass
class SwarmState:
    goal: str
    current_role: AgentRole = AgentRole.ROUTER
    turns: list[TurnRecord] = field(default_factory=list)
    artifacts: dict[str, Any] = field(default_factory=dict)

    def add_turn(self, record: TurnRecord) -> None:
        self.turns.append(record)
        if record.handoff is not None:
            self.current_role = record.handoff.next_role

    def last_turn(self) -> TurnRecord | None:
        return self.turns[-1] if self.turns else None


_JSON_OBJECT_RE = re.compile(r"\{[\s\S]*\}")


def parse_handoff_from_text(text: str) -> HandoffEnvelope | None:
    match = _JSON_OBJECT_RE.search(text)
    if not match:
        return None
    candidate = match.group(0)
    try:
        data = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    if data.get("type") != "handoff":
        return None
    if "next_role" not in data:
        return None
    return HandoffEnvelope.from_dict(data)


def format_handoff(handoff: HandoffEnvelope) -> str:
    payload: dict[str, Any] = {"type": "handoff", **handoff.to_dict()}
    return json.dumps(payload, ensure_ascii=False, indent=2)
