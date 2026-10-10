def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    group = {}
    for course, day in timetable:
        group.setdefault(day, []).append(course)
    for courses in group.values():
        courses.sort()
    return group
