"""Cross-member unit tests for Nguyen Dinh Hung (@benalexx007)'s Week 1 code (W2-4).

Tests Ben's Selection Sort algorithm translation (W1-4) and module edge cases.
"""

from members.benalexx007.w1 import grades, rules, text_tools, timetable, translate

# ============================================================================
# W1-4: Selection Sort Algorithm Tests
# ============================================================================


def test_selection_sort_empty() -> None:
    """Test selection sort on an empty list."""
    assert translate.selection_sort([]) == []


def test_selection_sort_single_element() -> None:
    """Test selection sort on a single-element list."""
    assert translate.selection_sort([42]) == [42]


def test_selection_sort_already_sorted() -> None:
    """Test selection sort on an already sorted list."""
    assert translate.selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_selection_sort_reversed() -> None:
    """Test selection sort on a reverse-sorted list."""
    assert translate.selection_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]


def test_selection_sort_with_duplicates() -> None:
    """Edge case: List containing duplicate elements and ties."""
    data = [4, 2, 5, 2, 3, 4, 1]
    assert translate.selection_sort(data) == [1, 2, 2, 3, 4, 4, 5]


def test_selection_sort_negative_numbers() -> None:
    """Edge case: List containing both negative and positive numbers."""
    data = [-3, 10, -50, 0, 8, -1]
    assert translate.selection_sort(data) == [-50, -3, -1, 0, 8, 10]


def test_selection_sort_in_place() -> None:
    """Verify that selection sort modifies and returns the exact same list instance."""
    original = [5, 1, 3]
    result = translate.selection_sort(original)
    assert result is original
    assert result == [1, 3, 5]


# ============================================================================
# Additional W1 Edge Case Tests for benalexx007
# ============================================================================


def test_grades_summary_even_length() -> None:
    """Edge case: Summary median calculation for even number of elements."""
    res = grades.summary([4.0, 6.0, 8.0, 10.0])
    assert res["min"] == 4.0
    assert res["max"] == 10.0
    assert res["mean"] == 7.0
    assert res["median"] == 7.0


def test_rules_missing_single_credit() -> None:
    """Edge case: Grammar boundary - 119 credits uses singular 'credit'."""
    reasons = rules.missing(119, 3.5)
    assert reasons == ["need 1 more credit"]


def test_rules_missing_multiple_credits() -> None:
    """Edge case: Grammar boundary - 118 credits uses plural 'credits'."""
    reasons = rules.missing(118, 1.5)
    assert "need 2 more credits" in reasons
    assert "need GPA of at least 2.0" in reasons


def test_text_tools_top_k_ties_alphabetical() -> None:
    """Edge case: Words with identical frequencies broken alphabetically."""
    text = "cat dog apple cat dog apple banana"
    # counts: apple: 2, cat: 2, dog: 2, banana: 1
    # top 3 words with freq 2 should be sorted alphabetically: apple, cat, dog
    assert text_tools.top_k(text, 3) == [("apple", 2), ("cat", 2), ("dog", 2)]


def test_timetable_by_day_sorting() -> None:
    """Edge case: Courses on the same day are returned sorted alphabetically."""
    entries = [("Math", "Monday"), ("Biology", "Monday"), ("Chemistry", "Monday")]
    assert timetable.by_day(entries) == {"Monday": ["Biology", "Chemistry", "Math"]}
