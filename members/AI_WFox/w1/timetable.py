# Expected time: O(n + C * sum(n_d log n_d)); space: O(n).
# n = entries; n_d = entries per day; C = maximum course-name length.


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    courses_by_day: dict[str, list[str]] = {}
    for course, day in timetable:
        courses_by_day.setdefault(day, []).append(course)
    for courses in courses_by_day.values():
        courses.sort()
    return courses_by_day
