from members.htbaax.w1 import grades, rules, text_tools, timetable, translate


def test_grade_summary():
    result = grades.summary([1, 2, 2])
    assert result["mean"] == 1.67
    assert result["median"] == 2


def test_text_tools():
    assert text_tools.word_count("!,.:?") == {}  # Edge case: punctuation-only input
    assert text_tools.top_k("banana apple banana apple", 2) == [("apple", 2), ("banana", 2)]


def test_thesis_eligibility():
    assert rules.can_register_thesis(120, 2.0)
    assert not rules.can_register_thesis(119, 2.0)
    assert len(rules.missing(119, 1.9)) == 2


def test_insertion_sort():
    numbers = [3, -1, 3, 0]
    result = translate.insertion_sort(numbers)
    assert result is numbers
    assert numbers == [-1, 0, 3, 3]


def test_timetable():
    courses = [("B", "Mon"), ("A", "Mon"), ("C", "Tue"), ("B", "Mon")]
    assert timetable.by_day(courses) == {"Mon": ["A", "B", "B"], "Tue": ["C"]}
