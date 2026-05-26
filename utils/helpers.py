"""General helper utilities."""

from __future__ import annotations

from datetime import datetime, timezone


def utc_compact_timestamp() -> str:
    """Return UTC timestamp in YYYYMMDDHHMMSS format."""
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


def format_duration(seconds: float) -> int:
    """Format runtime duration as rounded integer seconds."""
    return max(0, int(round(seconds)))
