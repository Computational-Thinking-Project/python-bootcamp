"""Parse ISO dates and simple relative due-date expressions."""

import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Resolve an ISO date, tomorrow, in N days or a Mon-Sun abbreviation.

    Surrounding whitespace and letter case are ignored. A weekday always
    means its next occurrence, even when it matches today. Unknown or
    invalid date strings raise ValueError.
    """
    text = text.strip().lower()

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return date.fromisoformat(text)

    if text == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in (\d+) days?", text)
    if match:
        return today + timedelta(days=int(match.group(1)))

    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    if text in weekdays:
        days = (weekdays.index(text) - today.weekday()) % 7
        if days == 0:
            days = 7
        return today + timedelta(days=days)

    raise ValueError(f"Unknown date: {text}")
