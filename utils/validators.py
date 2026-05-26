"""Validation helpers for lexeme dial-in."""

from __future__ import annotations

import re

_LEXEME_RE = re.compile(r"^[A-Za-z0-9_\-]+$")


def normalize_lexeme(value: str) -> str:
    """Normalize lexemes for case-insensitive lookup and alias matching."""
    cleaned = "".join(ch for ch in value if ch.isalnum())
    return cleaned.lower()


def is_valid_lexeme(value: str) -> bool:
    """Return True when lexeme is non-empty and only uses supported characters."""
    return bool(value and _LEXEME_RE.match(value))
