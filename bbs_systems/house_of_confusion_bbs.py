"""THE House of Confusion BBS flow."""

from __future__ import annotations

from typing import Callable, Dict, List


ROOMS = {
    "0": "THE Beacon",
    "1": "Shadow Entrance",
    "2": "As-Is Holding",
    "3": "Monkey Check",
    "4": "Coyote Cliff",
    "5": "Roadrunner Line",
    "9": "Exit Port",
}


def _monkey_check(input_func: Callable[[str], str], output_func: Callable[[str], None]) -> Dict[str, str]:
    output_func("\nThree Monkeys Check (safe/caution/blocked)")
    see = (input_func("see-no-harm: ").strip() or "safe").lower()
    hear = (input_func("hear-no-harm: ").strip() or "safe").lower()
    speak = (input_func("speak-no-harm: ").strip() or "safe").lower()
    return {"see": see, "hear": hear, "speak": speak}


def run(session: Dict, input_func: Callable[[str], str] = input, output_func: Callable[[str], None] = print) -> Dict:
    """Run the House of Confusion with exit-oriented routing."""
    output_func("\n=== THE HOUSE OF CONFUSION BBS ===")
    output_func("Enter as shadow. Exit with direction, pause, or safe disconnect.")

    entry = input_func("What are you entering as? (blank=shadow): ").strip()
    entry_state = "named" if entry else "shadow"

    monkeys = _monkey_check(input_func, output_func)
    rooms_visited: List[str] = ["Shadow Entrance", "Monkey Check"]

    while True:
        output_func("\nRooms: " + ", ".join(f"[{k}] {v}" for k, v in ROOMS.items()))
        choice = input_func("Route to room: ").strip()

        if choice not in ROOMS:
            output_func("Unknown room. Route again.")
            continue

        room = ROOMS[choice]
        rooms_visited.append(room)

        if choice == "2":
            fragment = input_func("As-is fragment: ").strip() or "silence"
            output_func(f"Fragment held: {fragment}")
        elif choice == "3":
            monkeys = _monkey_check(input_func, output_func)
            output_func("Monkey check refreshed.")
        elif choice == "4":
            output_func("Coyote Cliff logged as edge-discovery.")
        elif choice == "5":
            output_func("Roadrunner Line confirms continuation path.")
        elif choice == "9":
            break

    next_exit = input_func("Define your next exit (or pause): ").strip() or "pause"
    output_func(f"Exit recorded: {next_exit}")

    return {
        "entry_state": entry_state,
        "rooms_visited": rooms_visited,
        "signal": "house traversal complete",
        "monkeys": monkeys,
        "exit": next_exit,
    }
