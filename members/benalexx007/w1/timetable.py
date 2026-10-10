def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for course, day in timetable:
        grouped.setdefault(day, []).append(course)
    for courses in grouped.values():
        courses.sort()
    return grouped
