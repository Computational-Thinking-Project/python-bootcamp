"""Date parsing utilities for due date expressions (W3-1)."""

import re
from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
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
    """Parse due date text into a date object.

    Supports:
    - ISO format YYYY-MM-DD
    - "today", "tomorrow"
    - "in N days" / "in N day"
    - Weekday names (e.g., "Fri", "Wednesday") -> next occurrence (not today)
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Due date expression cannot be empty")

    lower = cleaned.lower()

    if lower == "today":
        return today

    if lower == "tomorrow":
        return today + timedelta(days=1)

    in_days_match = re.fullmatch(r"in\s+(\d+)\s+days?", lower)
    if in_days_match:
        days = int(in_days_match.group(1))
        return today + timedelta(days=days)

    if lower in WEEKDAYS:
        target_wd = WEEKDAYS[lower]
        delta = (target_wd - today.weekday()) % 7
        if delta == 0:
            delta = 7
        return today + timedelta(days=delta)

    try:
        return date.fromisoformat(cleaned)
    except ValueError as exc:
        raise ValueError(f"Unrecognized date expression: {text!r}") from exc
