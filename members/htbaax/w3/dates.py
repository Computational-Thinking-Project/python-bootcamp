"""Date parsing utilities for relative, weekday, and ISO due date expressions (W3-1)."""

import re
from datetime import date, timedelta

WEEKDAY_MAP: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a textual due date into a concrete datetime.date object.

    Supported patterns:
    - ISO 8601 date string (e.g. "2026-10-30")
    - Relative day terms: "today", "tomorrow"
    - Relative offset terms: "in N days" or "in N day" (N >= 0)
    - Weekday names (e.g. "Fri", "Tue", "Monday") resolving to the next strict occurrence

    Args:
        text: Due date expression string.
        today: Reference date used for relative date calculations.

    Returns:
        The resolved target date.

    Raises:
        ValueError: If text is empty, malformed, or cannot be parsed.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Due date string cannot be empty")

    normalized = cleaned.lower()

    if normalized == "today":
        return today

    if normalized == "tomorrow":
        return today + timedelta(days=1)

    in_days_match = re.fullmatch(r"in\s+(\d+)\s+days?", normalized)
    if in_days_match:
        offset_days = int(in_days_match.group(1))
        return today + timedelta(days=offset_days)

    if normalized in WEEKDAY_MAP:
        target_weekday = WEEKDAY_MAP[normalized]
        delta_days = (target_weekday - today.weekday()) % 7
        if delta_days == 0:
            delta_days = 7
        return today + timedelta(days=delta_days)

    try:
        return date.fromisoformat(cleaned)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Unrecognized date expression: {text!r}") from exc
