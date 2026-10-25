"""Comprehensive unit tests for htbaax Week 3 individual exercises."""

import io
from datetime import date
from pathlib import Path

import pytest

from members.htbaax.w3.cli import main
from members.htbaax.w3.dates import parse_due
from members.htbaax.w3.log_stats import analyse

BASE_DIR = Path(__file__).resolve().parents[3]
TASKS_CSV = BASE_DIR / "samples" / "tasks.csv"
REF_TODAY = date(2026, 10, 6)  # Tuesday


# ---------------------------------------------------------------------------
# W3-1: parse_due Tests
# ---------------------------------------------------------------------------


def test_parse_due_iso_dates() -> None:
    """Test standard ISO date parsing and leap years."""
    assert parse_due("2026-10-30", REF_TODAY) == date(2026, 10, 30)
    assert parse_due("2028-02-29", REF_TODAY) == date(2028, 2, 29)


def test_parse_due_relative_keywords() -> None:
    """Test 'today', 'tomorrow', and relative day offsets."""
    assert parse_due("today", REF_TODAY) == date(2026, 10, 6)
    assert parse_due("tomorrow", REF_TODAY) == date(2026, 10, 7)
    assert parse_due("in 1 day", REF_TODAY) == date(2026, 10, 7)
    assert parse_due("in 3 days", REF_TODAY) == date(2026, 10, 9)
    assert parse_due("in 0 days", REF_TODAY) == date(2026, 10, 6)


def test_parse_due_weekday_forward_jumping() -> None:
    """Weekday occurrences must strictly resolve into the future."""
    # REF_TODAY is Tuesday
    assert parse_due("Fri", REF_TODAY) == date(2026, 10, 9)
    assert parse_due("friday", REF_TODAY) == date(2026, 10, 9)
    # Next occurrence of today (Tuesday) must be 7 days later
    assert parse_due("Tue", REF_TODAY) == date(2026, 10, 13)
    assert parse_due("tuesday", REF_TODAY) == date(2026, 10, 13)
    # Yesterday's weekday (Monday) resolves to next week (6 days)
    assert parse_due("Mon", REF_TODAY) == date(2026, 10, 12)
    assert parse_due("Sunday", REF_TODAY) == date(2026, 10, 11)


def test_parse_due_invalid_inputs_raise_value_error() -> None:
    """Malformed dates and unrecognized keywords raise ValueError."""
    for invalid in ["", "   ", "someday", "next year", "in -2 days", "2026-02-31"]:
        with pytest.raises(ValueError):
            parse_due(invalid, REF_TODAY)


# ---------------------------------------------------------------------------
# W3-2: log_stats Tests
# ---------------------------------------------------------------------------


def test_log_stats_standard_dataset() -> None:
    """Verify request counts, nearest-rank p95, and slowest route."""
    pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    res = analyse(pairs)

    assert res["counts"]["fee"] == 3
    assert res["counts"]["rag"] == 2
    assert res["p95"]["fee"] == 300
    assert res["p95"]["rag"] == 1100
    assert res["slowest"] == "rag"


def test_log_stats_single_entry() -> None:
    """Single log entry yields p95 equal to its single latency."""
    res = analyse([("auth", 45)])
    assert res["counts"]["auth"] == 1
    assert res["p95"]["auth"] == 45
    assert res["slowest"] == "auth"


def test_log_stats_empty_input() -> None:
    """Empty log dataset returns empty structures with None slowest."""
    res = analyse([])
    assert len(res["counts"]) == 0
    assert res["p95"] == {}
    assert res["slowest"] is None


def test_log_stats_nearest_rank_distribution() -> None:
    """Verify nearest-rank calculation on larger sequence (1..100)."""
    # For N=100: rank = ceil(0.95 * 100) = 95 -> index 94 -> value 95
    pairs = [("query", i) for i in range(1, 101)]
    res = analyse(pairs)
    assert res["counts"]["query"] == 100
    assert res["p95"]["query"] == 95


# ---------------------------------------------------------------------------
# W3-3: CLI Tests
# ---------------------------------------------------------------------------


def test_cli_execution_success(capsys: pytest.CaptureFixture[str]) -> None:
    """CLI successfully plans tasks from samples/tasks.csv."""
    exit_code = main([str(TASKS_CSV), "--hours", "2", "--today", "2026-10-26"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Tonight (2.0 h):" in captured.out
    assert "1. Assignment" in captured.out
    assert "2. DS exam" in captured.out
    assert "1.5 h" in captured.out
    assert "0.5 h" in captured.out


def test_cli_missing_file_reports_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI exits with code 1 and writes to stderr when file does not exist."""
    stderr_stream = io.StringIO()
    monkeypatch.setattr("sys.stderr", stderr_stream)

    exit_code = main(["non_existent_tasks.csv", "--hours", "2"])
    assert exit_code == 1
    assert "Tasks file not found" in stderr_stream.getvalue()


def test_cli_negative_hours_reports_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI exits with code 1 when negative study hours are given."""
    stderr_stream = io.StringIO()
    monkeypatch.setattr("sys.stderr", stderr_stream)

    exit_code = main([str(TASKS_CSV), "--hours", "-1"])
    assert exit_code == 1
    assert "must be non-negative" in stderr_stream.getvalue()
