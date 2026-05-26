"""Lexeme registry loading and lookup."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

from utils.validators import normalize_lexeme


class LexemeManager:
    """Manage registry-backed lexeme resolution."""

    def __init__(self, registry_path: str | Path) -> None:
        self.registry_path = Path(registry_path)
        self.registry: Dict[str, dict] = {}
        self._lookup: Dict[str, str] = {}
        self.reload()

    def reload(self) -> None:
        """Reload registry from disk."""
        with self.registry_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        if not isinstance(data, dict):
            raise ValueError("Lexeme registry must be a JSON object")

        self.registry = data
        self._lookup.clear()

        for key, record in self.registry.items():
            normalized_key = normalize_lexeme(key)
            self._lookup[normalized_key] = key

            aliases = record.get("aliases", [])
            for alias in aliases:
                self._lookup[normalize_lexeme(alias)] = key

    def resolve(self, lexeme: str) -> Optional[dict]:
        """Resolve a lexeme or alias to a registry record."""
        key = self._lookup.get(normalize_lexeme(lexeme))
        if key is None:
            return None

        record = dict(self.registry[key])
        record["lexeme"] = key
        return record

    def validate(self, lexeme: str) -> bool:
        """Return True when lexeme can be resolved to a known record."""
        return self.resolve(lexeme) is not None

    def known_lexemes(self) -> List[str]:
        """Return sorted primary lexeme names."""
        return sorted(self.registry.keys())

    def suggestions(self, prefix: str) -> List[str]:
        """Return primary lexeme suggestions for an input prefix."""
        normalized_prefix = normalize_lexeme(prefix)
        if not normalized_prefix:
            return self.known_lexemes()

        matches = []
        for lexeme in self.known_lexemes():
            if normalize_lexeme(lexeme).startswith(normalized_prefix):
                matches.append(lexeme)
        return matches
