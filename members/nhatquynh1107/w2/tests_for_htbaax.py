"""Cross-test htbaax's Week 1 exercises, including punctuation-only text."""

from members.htbaax.w1 import grades, rules, text_tools, timetable, translate


def test_grade_summary() -> None:
    """Check rounding of the mean and selection of the median."""
    result = grades.summary([1, 2, 2])
    assert result["mean"] == 1.67
    assert result["median"] == 2


def test_text_tools() -> None:
    """Check punctuation-only input and alphabetical tie-breaking."""
    assert text_tools.word_count("!,.:?") == {}  # Edge case: punctuation-only input
    assert text_tools.top_k("banana apple banana apple", 2) == [
        ("apple", 2),
        ("banana", 2),
    ]


def test_thesis_eligibility() -> None:
    """Check eligibility boundaries and both unmet requirements."""
    assert rules.can_register_thesis(120, 2.0)
    assert not rules.can_register_thesis(119, 2.0)
    assert len(rules.missing(119, 1.9)) == 2


def test_insertion_sort() -> None:
    """Check that sorting handles duplicates and mutates the original list."""
    numbers = [3, -1, 3, 0]
    result = translate.insertion_sort(numbers)
    assert result is numbers
    assert numbers == [-1, 0, 3, 3]


def test_timetable() -> None:
    """Check grouping, alphabetical ordering and duplicate preservation."""
    courses = [("B", "Mon"), ("A", "Mon"), ("C", "Tue"), ("B", "Mon")]
    assert timetable.by_day(courses) == {"Mon": ["A", "B", "B"], "Tue": ["C"]}
