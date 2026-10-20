"""Date parsing utility module for handling natural language and ISO dates."""

import re
from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tues": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thur": 3,
    "thurs": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a date string into a date object relative to today.

    Supports:
        - ISO format: "YYYY-MM-DD" (e.g. "2026-10-30")
        - "today" -> today
        - "tomorrow" -> today + 1 day
        - "in N days" / "in N day" -> today + N days
        - Weekday names (e.g. "Fri", "Tuesday") -> next occurrence (strictly in the future)

    Args:
        text: Date string to parse.
        today: Reference date.

    Returns:
        Resolved date object.

    Raises:
        ValueError: If text cannot be parsed or represents an invalid date.
    """
    clean = text.strip()
    if not clean:
        raise ValueError("Due date string cannot be empty")

    # 1. ISO format date: YYYY-MM-DD
    if re.match(r"^\d{4}-\d{2}-\d{2}$", clean):
        try:
            return date.fromisoformat(clean)
        except ValueError as exc:
            raise ValueError(f"Invalid ISO date '{clean}': {exc}") from exc

    lower = clean.lower()

    # 2. Relative keywords: today, tomorrow
    if lower == "today":
        return today
    if lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. Relative offset: "in N days" / "in N day"
    offset_match = re.match(r"^in\s+(\d+)\s+days?$", lower)
    if offset_match:
        days = int(offset_match.group(1))
        return today + timedelta(days=days)

    # 4. Weekday names: next occurrence (if today is the same weekday, jump 7 days)
    if lower in WEEKDAYS:
        target_wd = WEEKDAYS[lower]
        current_wd = today.weekday()
        days_ahead = (target_wd - current_wd) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Cannot parse due date from unknown format: '{text}'")
