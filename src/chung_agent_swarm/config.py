from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class RuntimeConfig:
    anthropic_api_key: str | None


def load_runtime_config() -> RuntimeConfig:
    return RuntimeConfig(anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY"))
