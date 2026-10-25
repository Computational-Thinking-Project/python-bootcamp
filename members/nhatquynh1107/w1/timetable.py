"""Group course names by their scheduled day."""


def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Return alphabetically sorted course names per day, keeping duplicates."""
    byDay: dict[str, list[str]] = {}

    for course, day in entries:
        byDay.setdefault(day, []).append(course)

    for courses in byDay.values():
        courses.sort()

    return byDay
