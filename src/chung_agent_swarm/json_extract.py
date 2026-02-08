from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ExtractedJson:
    value: Any
    start: int
    end: int


class JsonExtractionError(ValueError):
    pass


def extract_first_json_value(text: str) -> ExtractedJson:
    decoder = json.JSONDecoder()

    for start in _candidate_starts(text):
        try:
            value, end_rel = decoder.raw_decode(text[start:])
        except json.JSONDecodeError:
            continue
        end = start + end_rel
        return ExtractedJson(value=value, start=start, end=end)

    raise JsonExtractionError("No valid JSON value found in input text.")


def _candidate_starts(text: str) -> list[int]:
    starts: list[int] = []
    for i, ch in enumerate(text):
        if ch in "{[":
            starts.append(i)
    return starts
