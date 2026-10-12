# Fixed cases: O(1) time/space; search sweep: O(m^3) time, O(m) space.
# m = maximum list length in the search sweep; excludes pytest overhead.

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest

MODULE_DIRECTORY = Path(__file__).resolve().parent


def load(module_name: str) -> ModuleType:
    module_spec = importlib.util.spec_from_file_location(
        f"local_w1_{module_name}", MODULE_DIRECTORY / f"{module_name}.py"
    )
    if module_spec is None or module_spec.loader is None:
        raise ImportError(f"Cannot load module: {module_name}")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


grades = load("grades")
text_tools = load("text_tools")
rules = load("rules")
translate = load("translate")
timetable = load("timetable")


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([7.5, 9, 6, 8], {"min": 6, "max": 9, "mean": 7.62, "median": 7.75}),
        ([4], {"min": 4, "max": 4, "mean": 4, "median": 4}),
        ([3, 1, 2], {"min": 1, "max": 3, "mean": 2, "median": 2}),
        ([-2, -4], {"min": -4, "max": -2, "mean": -3, "median": -3}),
        ([1.111, 1.119], {"min": 1.111, "max": 1.119, "mean": 1.11, "median": 1.11}),
    ],
)
def test_grade_summary(scores, expected):
    original_scores = scores.copy()
    assert grades.summary(scores) == expected
    assert scores == original_scores


def test_empty_grades():
    with pytest.raises(ValueError):
        grades.summary([])


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Git is fun. Git is fast!", {"git": 2, "is": 2, "fun": 1, "fast": 1}),
        ("  HELLO\nhello\tworld  ", {"hello": 2, "world": 1}),
        (
            "one,two;three:four!five?six.",
            dict.fromkeys(["one", "two", "three", "four", "five", "six"], 1),
        ),
        ("", {}),
        (" .,!?;: ", {}),
        ("Don't re-enter don't", {"don't": 2, "re-enter": 1}),
    ],
)
def test_word_count(text, expected):
    assert text_tools.word_count(text) == expected


@pytest.mark.parametrize(
    "text, k, expected",
    [
        ("Git is fun. Git is fast!", 2, [("git", 2), ("is", 2)]),
        ("z a z b a", 3, [("a", 2), ("z", 2), ("b", 1)]),
        ("b a", 10, [("a", 1), ("b", 1)]),
        ("b a", 0, []),
        ("b a", -1, []),
        ("", 2, []),
    ],
)
def test_top_k(text, k, expected):
    assert text_tools.top_k(text, k) == expected


@pytest.mark.parametrize(
    "credits, gpa, eligible",
    [
        (120, 2.0, True),
        (121, 3.5, True),
        (119, 2.0, False),
        (120, 1.999, False),
        (0, 0, False),
    ],
)
def test_thesis_thresholds(credits, gpa, eligible):
    assert rules.can_register_thesis(credits, gpa) is eligible
    assert bool(rules.missing(credits, gpa)) is not eligible


def test_missing_reasons():
    assert rules.missing(118, 2.0) == ["need 2 more credits"]
    assert rules.missing(119, 2.0) == ["need 1 more credit"]
    assert rules.missing(120, 1.9) == ["need GPA of at least 2.0"]
    assert rules.missing(118, 1.9) == [
        "need 2 more credits",
        "need GPA of at least 2.0",
    ]


@pytest.mark.parametrize(
    "values, key, expected",
    [([], 5, -1), ([5], 5, 0), ([5], 4, -1), ([1, 2, 2, 2, 3], 2, 2)],
)
def test_binary_search_examples(values, key, expected):
    original_values = values.copy()
    assert translate.binary_search(values, key) == expected
    assert values == original_values


def test_binary_search_against_linear_membership():
    for length in range(65):
        values = list(range(-length, length, 2))
        original_values = values.copy()
        for key in range(-length - 1, length + 2):
            result = translate.binary_search(values, key)
            expected = values.index(key) if key in values else -1
            assert result == expected
        assert values == original_values


@pytest.mark.parametrize(
    "entries, expected",
    [
        ([], {}),
        (
            [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")],
            {"Mon": ["CSC10001", "CSC10014"], "Tue": ["MTH00003"]},
        ),
        ([("B", "Fri"), ("A", "Fri"), ("A", "Fri")], {"Fri": ["A", "A", "B"]}),
    ],
)
def test_timetable(entries, expected):
    original_entries = entries.copy()
    assert timetable.by_day(entries) == expected
    assert entries == original_entries
