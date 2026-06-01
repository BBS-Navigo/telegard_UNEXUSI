"""Dialer interface orchestrating user input and connections."""

from __future__ import annotations

from typing import Callable, Dict, List

from core.connection_manager import ConnectionManager
from core.lexeme_manager import LexemeManager
from ui.animations import connection_sequence


class Dialer:
    """Main dialer state for lexeme-driven connection attempts."""

    def __init__(
        self,
        lexeme_manager: LexemeManager,
        connection_manager: ConnectionManager,
        max_history: int = 20,
        connection_delay: float = 0.2,
    ) -> None:
        self.lexeme_manager = lexeme_manager
        self.connection_manager = connection_manager
        self.max_history = max_history
        self.connection_delay = connection_delay
        self.history: List[str] = []

    def autocomplete(self, prefix: str) -> List[str]:
        """Return known lexeme suggestions."""
        return self.lexeme_manager.suggestions(prefix)

    def record_history(self, lexeme: str) -> None:
        """Track latest dial attempts in bounded history."""
        self.history.append(lexeme)
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history :]

    def dial(
        self,
        lexeme: str,
        input_func: Callable[[str], str] = input,
        output_func: Callable[[str], None] = print,
    ) -> Dict:
        """Dial a lexeme, run connection animation, and connect."""
        self.record_history(lexeme)
        connection_sequence(output_func=output_func, delay=self.connection_delay)
        return self.connection_manager.connect(lexeme, input_func=input_func, output_func=output_func)
