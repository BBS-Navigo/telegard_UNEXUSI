"""Quantum Telegard lexeme dial-up terminal entry point."""

from __future__ import annotations

import json
from pathlib import Path

from core.connection_manager import ConnectionManager
from core.dialer import Dialer
from core.lexeme_manager import LexemeManager
from core.session_logger import SessionLogger
from ui.terminal_ui import show_help, show_splash


def _load_config(config_path: Path) -> dict:
    """Load lightweight config from YAML-like file with JSON fallback defaults."""
    defaults = {
        "terminal": {"splash": True, "connection_delay_seconds": 0.2, "max_history": 20},
        "logging": {"session_log_path": "logs/sessions.log"},
    }

    if not config_path.exists():
        return defaults

    # Keep parser dependency-free: if YAML syntax is present we use defaults,
    # and if JSON content is provided (even in .yaml) we merge it.
    text = config_path.read_text(encoding="utf-8")
    if text.strip().startswith("{"):
        try:
            loaded = json.loads(text)
            defaults.update(loaded)
            return defaults
        except json.JSONDecodeError:
            return defaults

    return defaults


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    config = _load_config(base_dir / "config" / "dialup_config.yaml")

    lexeme_manager = LexemeManager(base_dir / "config" / "lexeme_registry.json")
    session_logger = SessionLogger(base_dir / config["logging"]["session_log_path"])
    connection_manager = ConnectionManager(lexeme_manager, session_logger)

    terminal_cfg = config.get("terminal", {})
    dialer = Dialer(
        lexeme_manager,
        connection_manager,
        max_history=int(terminal_cfg.get("max_history", 20)),
        connection_delay=float(terminal_cfg.get("connection_delay_seconds", 0.2)),
    )

    if terminal_cfg.get("splash", True):
        show_splash()

    show_help()

    while True:
        raw = input("\nlexeme-dial> ").strip()
        if not raw:
            continue

        command = raw.lower()
        if command in {"quit", "exit"}:
            print("Disconnecting terminal. Safe travels.")
            break

        if command == "help":
            show_help()
            continue

        if command == "list":
            print("Known lexemes:", ", ".join(lexeme_manager.known_lexemes()))
            continue

        if command == "history":
            if not dialer.history:
                print("No dial history yet.")
            else:
                print("Recent dials:", ", ".join(dialer.history))
            continue

        suggestions = dialer.autocomplete(raw)
        if not suggestions:
            print("Unknown lexeme. Try 'list' for known entries.")
            continue

        summary = dialer.dial(raw)
        print(f"Session complete: status={summary['connection_status']} exit={summary.get('exit', 'disconnect')}")


if __name__ == "__main__":
    main()
