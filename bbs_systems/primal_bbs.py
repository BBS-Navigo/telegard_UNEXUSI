"""Primal BBS system implementation."""

from __future__ import annotations

from typing import Callable, Dict, List


MENU = {
    "1": ("THE Beacon", "Enter the intake beacon"),
    "2": ("Archive", "Read prior primal signals"),
    "3": ("Exit Port", "Disconnect from Primal"),
}


def _show_menu(output_func: Callable[[str], None]) -> None:
    output_func("\n--- PRIMAL MAIN MENU ---")
    for key, (_room, description) in MENU.items():
        output_func(f"[{key}] {description}")


def run(session: Dict, input_func: Callable[[str], str] = input, output_func: Callable[[str], None] = print) -> Dict:
    """Run the Primal BBS text menu."""
    output_func("\n=== PRIMAL BBS ===")
    output_func("Connection established. You are in primal signal space.")

    handle = input_func("Handle (blank for shadow): ").strip()
    entry_state = "named" if handle else "shadow"
    if not handle:
        handle = "shadow"

    output_func(f"Welcome, {handle}.")

    rooms_visited: List[str] = ["Primal Lobby"]
    signal = "silent"

    while True:
        _show_menu(output_func)
        choice = input_func("Select [1-3]: ").strip()
        room = MENU.get(choice)

        if room is None:
            output_func("Invalid selection. Try again.")
            continue

        room_name = room[0]
        rooms_visited.append(room_name)

        if choice == "1":
            signal = input_func("THE Beacon signal: ").strip() or "silence"
            output_func("Signal received and held as-is.")
        elif choice == "2":
            output_func("Archive: [placeholder] prior primal entries will appear here.")
        elif choice == "3":
            output_func("Exiting Primal via Exit Port.")
            break

    return {
        "entry_state": entry_state,
        "rooms_visited": rooms_visited,
        "signal": signal,
        "exit": "disconnect",
    }
