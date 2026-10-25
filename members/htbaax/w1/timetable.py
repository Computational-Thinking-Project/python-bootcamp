"""Timetable grouping by day (W1-5)."""


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day of week and sort courses alphabetically within each day."""
    result: dict[str, list[str]] = {}

    for course, day in timetable:
        result.setdefault(day, []).append(course)

    for courses in result.values():
        courses.sort()

    return result
