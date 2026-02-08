from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version


def _get_version() -> str:
    try:
        return version("chung-agent-swarm")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = _get_version()

__all__ = ["__version__"]
