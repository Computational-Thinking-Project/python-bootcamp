from members.thanhdat3010.w1.grades import summary
from members.thanhdat3010.w1.rules import missing
from members.thanhdat3010.w1.text_tools import top_k
from members.thanhdat3010.w1.timetable import by_day
from members.thanhdat3010.w1.translate import bfs


def test_grades_summary() -> None:
    """Check score statistics for repeated and unsorted values."""
    # Test 01
    scores = [4, 4, 4]
    expected_summary = {
        "min": 4,
        "max": 4,
        "mean": 4.0,
        "median": 4.0,
    }
    assert summary(scores) == expected_summary

    # Test 02
    scores = [9, 1, 3]
    expected_summary = {
        "min": 1,
        "max": 9,
        "mean": 4.33,
        "median": 3.0,
    }
    assert summary(scores) == expected_summary


def test_text_tools_top_k() -> None:
    """Check punctuation-only input and non-positive or limited word counts."""
    # Test 01
    text = ".,!.?.,!,,?"
    assert top_k(text, 3) == []

    # Test 02
    text = "Apple apple banana"
    assert top_k(text, 0) == []

    # Test 03
    expected_answers = [("apple", 2)]
    assert top_k(text, 1) == expected_answers


def test_rules_missing() -> None:
    """Check missing thesis requirements at the credit and GPA boundaries."""
    # Test 01
    credits = 119
    gpa = 2.0
    expected_reasons = ["need 1 more credits"]
    assert missing(credits, gpa) == expected_reasons

    # Test 02
    credits = 120
    gpa = 1.99
    expected_reasons = []
    assert missing(credits, gpa) != expected_reasons


def test_bfs_cycle_and_disconnected_nodes() -> None:
    """Check BFS with cycles, disconnected nodes, and repeated edges."""
    # Test 01
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["D"],
        "D": [],
        "X": ["Y"],
        "Y": [],
    }

    assert bfs(graph, "A") == ["A", "B", "C", "D"]

    # Test 02
    graph = {"A": ["A", "B", "B"], "B": []}

    assert bfs(graph, "A") == ["A", "B"]


def test_timetable_by_day() -> None:
    """Check sorted course groups and preservation of duplicate entries."""
    # Test 01
    timetable = [
        ("Z", "Monday"),
        ("A", "Monday"),
        ("B", "Tuesday"),
        ("C", "Tuesday"),
        ("D", "Wednesday"),
    ]

    expected_schedule = {
        "Monday": ["A", "Z"],
        "Tuesday": ["B", "C"],
        "Wednesday": ["D"],
    }

    assert by_day(timetable) == expected_schedule

    # Test 02
    timetable = [("CS", "Mon"), ("CS", "Mon")]

    expected_schedule = {"Mon": ["CS", "CS"]}

    assert by_day(timetable) == expected_schedule
