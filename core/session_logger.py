"""Session logging for lexeme dial-in attempts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


class SessionLogger:
    """Write session events as JSON-lines for audit and replay."""

    def __init__(self, log_path: str | Path) -> None:
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def log_session(self, payload: Dict) -> None:
        """Append one structured session record."""
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
