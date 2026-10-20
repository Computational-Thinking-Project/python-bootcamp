import re
from datetime import date, datetime, timedelta


def is_valid_date(text: str, date_format: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(text, date_format)
        return True
    except ValueError:
        return False


def is_valid_text(text: str, pattern: str =r"^in\s+\d+\s+days$") -> bool:
    return bool(re.fullmatch(pattern, text, re.IGNORECASE))


def parse_due(text: str, today: date) -> date:
    weekdays = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

    if text == "tomorrow":
        target_date = today + timedelta(days=1)
        return target_date
    elif is_valid_date(text):
        return datetime.strptime(text, "%Y-%m-%d").date()
    elif text in weekdays:
        target_weekday = weekdays[text]
        current_weekday = today.weekday()

        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:
            days_ahead += 7

        target_date = today + timedelta(days=days_ahead)
        return target_date
    elif is_valid_text(text):
        match = re.search(r"\d+", text)
        if match:
            days_ahead = int(match.group())
            target_date = today + timedelta(days=days_ahead)
            return target_date
    else:
        raise ValueError("Invalid input")
