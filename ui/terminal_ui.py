"""Terminal UI rendering utilities."""

from __future__ import annotations

from typing import Callable

from ui.ascii_art import DIVIDER, SPLASH


def show_splash(output_func: Callable[[str], None] = print) -> None:
    output_func(SPLASH)
    output_func(DIVIDER)
    output_func("Lexeme Dial-Up Terminal :: shadow entrance / exit-oriented")
    output_func(DIVIDER)


def show_help(output_func: Callable[[str], None] = print) -> None:
    output_func("Commands:")
    output_func("  list      - show known lexemes")
    output_func("  history   - show dial history")
    output_func("  help      - show this help")
    output_func("  quit      - exit terminal")
    output_func("  <lexeme>  - dial into BBS")
