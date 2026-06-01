"""Template BBS implementation for new systems."""

from __future__ import annotations

from typing import Callable, Dict


def run(session: Dict, input_func: Callable[[str], str] = input, output_func: Callable[[str], None] = print) -> Dict:
    """Template run loop demonstrating required return structure."""
    output_func("=== TEMPLATE BBS ===")
    output_func("Replace this module with your system-specific logic.")

    name = input_func("Caller handle (optional): ").strip()
    if not name:
        name = "shadow"

    output_func(f"Welcome, {name}. This template exits immediately.")

    return {
        "entry_state": "shadow" if name == "shadow" else "named",
        "rooms_visited": ["Template Welcome", "Template Exit"],
        "signal": "Template loop complete",
        "exit": "disconnect",
    }
