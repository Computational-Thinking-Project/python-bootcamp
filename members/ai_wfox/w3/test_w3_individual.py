"""Comprehensive unit tests for week 3 individual exercises."""

import sys
from datetime import date
from pathlib import Path

import pytest

BOOTCAMP = Path(__file__).resolve().parents[3]
if str(BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP))

from members.ai_wfox.w3.cli import main as cli_main
from members.ai_wfox.w3.dates import parse_due
from members.ai_wfox.w3.log_stats import analyse

TODAY = date(2026, 10, 6)  # Tuesday


def test_parse_due_standard() -> None:
    """Test standard date strings and relative expressions."""
    assert parse_due("2026-10-30", TODAY) == date(2026, 10, 30)
    assert parse_due("tomorrow", TODAY) == date(2026, 10, 7)
    assert parse_due("today", TODAY) == date(2026, 10, 6)
    assert parse_due("in 3 days", TODAY) == date(2026, 10, 9)
    assert parse_due("in 1 day", TODAY) == date(2026, 10, 7)
    assert parse_due("Fri", TODAY) == date(2026, 10, 9)
    assert parse_due("Tue", TODAY) == date(2026, 10, 13)


def test_parse_due_all_weekdays() -> None:
    """Test next occurrence calculation across all weekdays."""
    # TODAY is Tuesday (1)
    assert parse_due("Wednesday", TODAY) == date(2026, 10, 7)
    assert parse_due("Thursday", TODAY) == date(2026, 10, 8)
    assert parse_due("Friday", TODAY) == date(2026, 10, 9)
    assert parse_due("Saturday", TODAY) == date(2026, 10, 10)
    assert parse_due("Sunday", TODAY) == date(2026, 10, 11)
    assert parse_due("Monday", TODAY) == date(2026, 10, 12)
    assert parse_due("Tuesday", TODAY) == date(2026, 10, 13)


def test_parse_due_invalid() -> None:
    """Test invalid and empty date inputs raise ValueError."""
    with pytest.raises(ValueError):
        parse_due("someday", TODAY)
    with pytest.raises(ValueError):
        parse_due("", TODAY)
    with pytest.raises(ValueError):
        parse_due("   ", TODAY)
    with pytest.raises(ValueError):
        parse_due("2026-02-30", TODAY)


def test_log_stats_standard() -> None:
    """Test log stats analysis with typical routing data."""
    pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    res = analyse(pairs)
    assert res["counts"] == {"fee": 3, "rag": 2}
    assert res["slowest"] == "rag"
    assert res["p95"]["fee"] == 300
    assert res["p95"]["rag"] == 1100


def test_log_stats_empty() -> None:
    """Test log stats analysis on empty input."""
    res = analyse([])
    assert len(res["counts"]) == 0
    assert res["p95"] == {}
    assert res["slowest"] is None


def test_log_stats_single() -> None:
    """Test log stats analysis with a single log entry."""
    res = analyse([("search", 42)])
    assert res["counts"]["search"] == 1
    assert res["p95"]["search"] == 42
    assert res["slowest"] == "search"


def test_cli_execution_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Test CLI happy path produces scheduled output."""
    sample_csv = BOOTCAMP / "samples" / "tasks.csv"
    code = cli_main([str(sample_csv), "--hours", "2", "--today", "2026-10-26"])
    assert code == 0
    captured = capsys.readouterr()
    assert "Tonight (2.0 h):" in captured.out
    assert "Assignment" in captured.out
    assert "DS exam" in captured.out


def test_cli_missing_file() -> None:
    """Test CLI returns exit code 1 when tasks file is missing."""
    code = cli_main(["missing_file.csv", "--hours", "2"])
    assert code == 1


def test_cli_invalid_today() -> None:
    """Test CLI returns exit code 1 on invalid --today argument."""
    sample_csv = BOOTCAMP / "samples" / "tasks.csv"
    code = cli_main([str(sample_csv), "--hours", "2", "--today", "invalid-date"])
    assert code == 1


def test_cli_negative_hours() -> None:
    """Test CLI returns exit code 1 on negative --hours argument."""
    sample_csv = BOOTCAMP / "samples" / "tasks.csv"
    code = cli_main([str(sample_csv), "--hours", "-1"])
    assert code == 1
