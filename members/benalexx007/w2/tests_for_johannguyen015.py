"""Cross-member unit tests for Nguyen Ba Duy (@johannguyen015)'s Week 1 code (W2-4).

Tests Duy's Sieve of Eratosthenes algorithm translation and edge cases across their W1 modules.
"""

from __future__ import annotations

import pytest

from members.johannguyen015.w1 import grades, rules, text_tools, timetable, translate


def test_duy_sieve_standard_primes() -> None:
    """Test standard Sieve of Eratosthenes execution up to 10 and 20."""
    assert translate.primes_up_to(10) == [2, 3, 5, 7]
    assert translate.primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_duy_sieve_boundary_and_negative() -> None:
    """Edge cases: test with 2, 1, 0, and negative numbers."""
    assert translate.primes_up_to(2) == [2]
    assert translate.primes_up_to(1) == []
    assert translate.primes_up_to(0) == []
    assert translate.primes_up_to(-10) == []


def test_duy_grades_summary() -> None:
    """Test grade statistics and rounding to 2 decimals."""
    res = grades.summary([7.5, 9, 6, 8])
    assert res["min"] == 6
    assert res["max"] == 9
    assert res["mean"] == 7.62
    assert res["median"] == 7.75

    even_res = grades.summary([8.0, 9.0, 7.0, 10.0])
    assert even_res["median"] == 8.5


def test_duy_grades_empty_error() -> None:
    """Test that empty scores list raises ValueError."""
    with pytest.raises(ValueError):
        grades.summary([])


def test_duy_rules_thesis_eligibility() -> None:
    """Test thesis registration criteria and missing requirements messages."""
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(119, 2.5) is False
    assert rules.can_register_thesis(130, 1.99) is False

    missing_msgs = rules.missing(115, 1.8)
    assert any("5 more credits" in m for m in missing_msgs)
    assert any("GPA" in m for m in missing_msgs)


def test_duy_text_tools_word_count_and_top_k() -> None:
    """Test word count with punctuation stripping and top_k tie-breaking."""
    text = "Apple, banana! Apple; orange? banana."
    counts = text_tools.word_count(text)
    assert counts["apple"] == 2
    assert counts["banana"] == 2
    assert counts["orange"] == 1

    # Tie breaking: apple and banana both have 2, 'apple' comes before 'banana'
    top = text_tools.top_k(text, 2)
    assert top == [("apple", 2), ("banana", 2)]


def test_duy_timetable_by_day() -> None:
    """Test course grouping by day with sorted course names."""
    entries = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    grouped = timetable.by_day(entries)
    assert grouped == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }
