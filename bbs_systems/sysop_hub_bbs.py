"""SYSOP Hub BBS flow."""

from __future__ import annotations

from typing import Callable, Dict, List


MENU = {
    "1": "Ops Board",
    "2": "Node Status",
    "3": "Carrier Drop",
}


def _show_menu(output_func: Callable[[str], None]) -> None:
    output_func("\n--- SYSOP HUB ---")
    output_func("[1] Ops Board")
    output_func("[2] Node Status")
    output_func("[3] Carrier Drop")


def run(session: Dict, input_func: Callable[[str], str] = input, output_func: Callable[[str], None] = print) -> Dict:
    """Run a simple old-school sysop terminal loop."""
    output_func("\n=== SYSOP HUB BBS ===")
    output_func("Console online. Keep it simple. Keep it live.")

    handle = input_func("Sysop handle (blank=shadow): ").strip()
    entry_state = "named" if handle else "shadow"
    if not handle:
        handle = "shadow"

    output_func(f"Welcome, {handle}.")

    rooms_visited: List[str] = ["Sysop Switchboard"]
    signal = "standing by"

    while True:
        _show_menu(output_func)
        choice = input_func("Select [1-3]: ").strip()
        room = MENU.get(choice)
        if room is None:
            output_func("Invalid selection. Re-route.")
            continue

        rooms_visited.append(room)

        if choice == "1":
            signal = input_func("Post ops note: ").strip() or "standing by"
            output_func("Ops note posted.")
        elif choice == "2":
            output_func("Node Status: uplink=green, archives=warm, modem=tone-locked")
        elif choice == "3":
            output_func("Carrier dropped. Returning to dial prompt.")
            break

    return {
        "entry_state": entry_state,
        "rooms_visited": rooms_visited,
        "signal": signal,
        "exit": "disconnect",
    }
