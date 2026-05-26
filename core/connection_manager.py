"""Connection routing and session lifecycle management."""

from __future__ import annotations

import traceback
from time import perf_counter
from typing import Callable, Dict

from bbs_systems.house_of_confusion_bbs import run as house_run
from bbs_systems.primal_bbs import run as primal_run
from bbs_systems.template_bbs import run as template_run
from core.lexeme_manager import LexemeManager
from core.session_logger import SessionLogger
from utils.helpers import format_duration, utc_compact_timestamp


class ConnectionManager:
    """Route lexeme dial-ins to concrete BBS implementations."""

    def __init__(self, lexeme_manager: LexemeManager, session_logger: SessionLogger) -> None:
        self.lexeme_manager = lexeme_manager
        self.session_logger = session_logger
        self.systems: Dict[str, Callable] = {
            "primal_bbs": primal_run,
            "house_of_confusion_bbs": house_run,
            "template_bbs": template_run,
        }

    def connect(
        self,
        lexeme: str,
        input_func: Callable[[str], str] = input,
        output_func: Callable[[str], None] = print,
    ) -> Dict:
        """Connect to a BBS endpoint by lexeme and return a session summary."""
        start = perf_counter()
        timestamp = utc_compact_timestamp()

        record = self.lexeme_manager.resolve(lexeme)
        if record is None:
            summary = {
                "timestamp": timestamp,
                "lexeme_dialed": lexeme,
                "connection_status": "failed",
                "session_duration": 0,
                "entry_state": "shadow",
                "rooms_visited": [],
                "signature": "Living Flame Script",
                "reason": "unknown_lexeme",
            }
            self.session_logger.log_session(summary)
            return summary

        if record.get("status") != "active":
            summary = {
                "timestamp": timestamp,
                "lexeme_dialed": record["lexeme"],
                "connection_status": "failed",
                "session_duration": 0,
                "entry_state": "shadow",
                "rooms_visited": [],
                "signature": "Living Flame Script",
                "reason": "inactive_lexeme",
            }
            self.session_logger.log_session(summary)
            return summary

        endpoint = record.get("endpoint")
        target = self.systems.get(endpoint)
        if target is None:
            summary = {
                "timestamp": timestamp,
                "lexeme_dialed": record["lexeme"],
                "connection_status": "failed",
                "session_duration": 0,
                "entry_state": "shadow",
                "rooms_visited": [],
                "signature": "Living Flame Script",
                "reason": "missing_endpoint",
            }
            self.session_logger.log_session(summary)
            return summary

        try:
            system_result = target({"lexeme": record["lexeme"], "record": record}, input_func=input_func, output_func=output_func)
            status = "success"
        except Exception as exc:  # pragma: no cover
            output_func("Connection aborted due to unexpected system error.")
            output_func(str(exc))
            output_func(traceback.format_exc())
            system_result = {
                "entry_state": "shadow",
                "rooms_visited": [],
                "signal": "error",
                "exit": "disconnect",
            }
            status = "failed"

        summary = {
            "timestamp": timestamp,
            "lexeme_dialed": record["lexeme"],
            "connection_status": status,
            "session_duration": format_duration(perf_counter() - start),
            "entry_state": system_result.get("entry_state", "shadow"),
            "rooms_visited": system_result.get("rooms_visited", []),
            "signal": system_result.get("signal", "silence"),
            "exit": system_result.get("exit", "disconnect"),
            "signature": "Living Flame Script",
        }

        if "monkeys" in system_result:
            summary["monkeys"] = system_result["monkeys"]

        self.session_logger.log_session(summary)
        return summary
