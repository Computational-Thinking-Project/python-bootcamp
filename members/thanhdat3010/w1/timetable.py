def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Given a list of (course, day) tuples, return a dictionary mapping each day
    to a sorted list of courses scheduled on that day.
    """
    schedule: dict[str, list[str]] = {}
    for course, day in entries:
        schedule.setdefault(day, []).append(course)

    for courses in schedule.values():
        courses.sort()

    return schedule
