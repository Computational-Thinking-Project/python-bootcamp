def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    byDay = {}

    for course, day in entries:
        byDay.setdefault(day, []).append(course)

    for courses in byDay.values():
        courses.sort()

    return byDay
