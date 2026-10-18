"""Cross-member unit tests for Tran Quang Tam (@AI-WFox)'s Week 1 code (W2-4).

Tests Tam's Binary Search algorithm translation (W1-4) and module edge cases.
"""

from members.ai_wfox.w1 import grades, rules, text_tools, timetable, translate

# ============================================================================
# W1-4: Binary Search Algorithm Tests (ai_wfox)
# ============================================================================


def test_binary_search_finds_middle_element() -> None:
    """Test binary search finding the middle element."""
    assert translate.binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_finds_first_element() -> None:
    """Test binary search finding the first element in sorted array."""
    assert translate.binary_search([1, 3, 5, 7, 9], 1) == 0


def test_binary_search_finds_last_element() -> None:
    """Test binary search finding the last element in sorted array."""
    assert translate.binary_search([1, 3, 5, 7, 9], 9) == 4


def test_binary_search_element_not_found() -> None:
    """Test binary search returning -1 when key is absent."""
    assert translate.binary_search([1, 3, 5, 7, 9], 4) == -1
    assert translate.binary_search([1, 3, 5, 7, 9], 0) == -1
    assert translate.binary_search([1, 3, 5, 7, 9], 100) == -1


def test_binary_search_empty_list() -> None:
    """Edge case: Searching in an empty list returns -1."""
    assert translate.binary_search([], 42) == -1


def test_binary_search_single_element() -> None:
    """Edge case: Single-element list found and not found."""
    assert translate.binary_search([10], 10) == 0
    assert translate.binary_search([10], 5) == -1


def test_binary_search_negative_numbers() -> None:
    """Edge case: Sorted array with negative numbers."""
    assert translate.binary_search([-50, -20, -5, 0, 15, 30], -5) == 2


# ============================================================================
# Additional W1 Edge Case Tests for ai_wfox
# ============================================================================


def test_summary_unsorted_scores() -> None:
    """Verify summary correctly sorts before computing median and stats."""
    assert grades.summary([10, 2, 6]) == {
        "min": 2,
        "max": 10,
        "mean": 6,
        "median": 6,
    }


def test_word_count_comma_without_space() -> None:
    """Verify word_count splits tokens separated by commas."""
    assert text_tools.word_count("red,blue") == {
        "red": 1,
        "blue": 1,
    }


def test_top_k_returns_only_requested_number() -> None:
    """Verify top_k respects the limit parameter."""
    assert text_tools.top_k("a b a c b a", 1) == [
        ("a", 3),
    ]


def test_missing_when_both_requirements_are_not_met() -> None:
    """Verify missing reports both credit and GPA deficits."""
    assert rules.missing(100, 1.5) == [
        "need 20 more credits",
        "need GPA of at least 2.0",
    ]


def test_timetable_sorts_courses_on_each_day() -> None:
    """Verify courses on the same day are sorted alphabetically."""
    assert timetable.by_day(
        [
            ("MTH00003", "Tue"),
            ("CSC10014", "Mon"),
            ("CSC10001", "Mon"),
        ]
    ) == {
        "Tue": ["MTH00003"],
        "Mon": ["CSC10001", "CSC10014"],
    }
