"""Parse the deadline formats required by W3-1."""

import re
from datetime import date, timedelta

WEEKDAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")


def parse_due(text: str, today: date) -> date:
    """Parse ISO dates, tomorrow, in N days, or the next abbreviated weekday.

    A weekday matching today means seven days later. Unknown formats raise
    ValueError; relative dates always use the supplied reference date.
    """
    value = text.strip().lower()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return date.fromisoformat(value)
    if value == "tomorrow":
        return today + timedelta(days=1)
    relative = re.fullmatch(r"in (\d+) days", value)
    if relative:
        return today + timedelta(days=int(relative.group(1)))
    if value in WEEKDAYS:
        days = (WEEKDAYS.index(value) - today.weekday()) % 7 or 7
        return today + timedelta(days=days)
    raise ValueError(f"Unknown due date: {text!r}")
