"""General helper utilities."""

from __future__ import annotations

from datetime import datetime, timezone


def utc_compact_timestamp() -> str:
    """Return UTC timestamp in YYYYMMDDHHMMSS format."""
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


def round_duration_seconds(seconds: float) -> int:
    """Return runtime duration rounded to integer seconds."""
    return max(0, int(round(seconds)))
