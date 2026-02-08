from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SessionConfigValidation:
    ok: bool
    errors: tuple[str, ...]


SESSION_CONFIG_TEMPLATE: dict[str, Any] = {
    "document_first": {
        "menu_file": ".claude/docs/claud_platform_menu.md",
        "relevant_specs": [],
        "notes": "",
    },
    "json_schema_definition": {"requirements": [], "references": []},
    "context_window_optimization": {"requirements": [], "references": []},
}


def load_session_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_session_config(data: Any) -> SessionConfigValidation:
    errors: list[str] = []

    if not isinstance(data, dict):
        return SessionConfigValidation(ok=False, errors=("Root must be a JSON object.",))

    _require_dict(data, "document_first", errors)
    _require_dict(data, "json_schema_definition", errors)
    _require_dict(data, "context_window_optimization", errors)

    doc_first = data.get("document_first")
    if isinstance(doc_first, dict):
        _require_str(doc_first, "menu_file", errors, "document_first.menu_file")
        _require_list(doc_first, "relevant_specs", errors, "document_first.relevant_specs")
        _require_str(doc_first, "notes", errors, "document_first.notes")

    for key in ("json_schema_definition", "context_window_optimization"):
        section = data.get(key)
        if isinstance(section, dict):
            _require_list(section, "requirements", errors, f"{key}.requirements")
            _require_list(section, "references", errors, f"{key}.references")

    return SessionConfigValidation(ok=len(errors) == 0, errors=tuple(errors))


def write_session_config_template(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(SESSION_CONFIG_TEMPLATE, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _require_dict(obj: dict[str, Any], key: str, errors: list[str]) -> None:
    if key not in obj:
        errors.append(f"Missing required key: {key}")
        return
    if not isinstance(obj.get(key), dict):
        errors.append(f"Key must be an object: {key}")


def _require_str(obj: dict[str, Any], key: str, errors: list[str], label: str) -> None:
    val = obj.get(key)
    if not isinstance(val, str):
        errors.append(f"Key must be a string: {label}")


def _require_list(obj: dict[str, Any], key: str, errors: list[str], label: str) -> None:
    val = obj.get(key)
    if not isinstance(val, list):
        errors.append(f"Key must be a list: {label}")
