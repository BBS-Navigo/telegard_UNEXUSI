"""Simple terminal animations."""

from __future__ import annotations

import time
from typing import Callable


def connection_sequence(output_func: Callable[[str], None] = print, sleep_func: Callable[[float], None] = time.sleep, delay: float = 0.2) -> None:
    """Render a simple dial-up style connection sequence."""
    for line in [
        "ATZ",
        "OK",
        "ATDT LEXEME",
        "CONNECT 9600",
        "CARRIER DETECTED",
    ]:
        output_func(line)
        sleep_func(delay)
