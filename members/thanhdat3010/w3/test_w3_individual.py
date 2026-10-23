"""Supplementary boundary tests; instructor tests are left unchanged."""

import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from members.thanhdat3010.w1.translate import bfs
from members.thanhdat3010.w3.dates import parse_due
from members.thanhdat3010.w3.log_stats import analyse

ROOT = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize(
    "text,today,expected",
    [
        ("tomorrow", date(2026, 12, 31), date(2027, 1, 1)),
        ("in 0 days", date(2026, 10, 6), date(2026, 10, 6)),
        (" Tue ", date(2026, 10, 6), date(2026, 10, 13)),
        ("in 2 days", date(2028, 2, 28), date(2028, 3, 1)),
    ],
)
def test_date_boundaries(text: str, today: date, expected: date) -> None:
    assert parse_due(text, today) == expected


@pytest.mark.parametrize("text", ["2026-02-29", "in -1 days", "someday", ""])
def test_invalid_dates(text: str) -> None:
    with pytest.raises(ValueError):
        parse_due(text, date(2026, 10, 6))


def test_percentile_rank_and_empty_logs() -> None:
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}
    stats = analyse(("fee", n) for n in range(1, 21))
    assert stats == {"counts": {"fee": 20}, "p95": {"fee": 19}, "slowest": "fee"}
    assert analyse([("first", 10), ("second", 10)])["slowest"] == "first"


@pytest.mark.parametrize("hours", ["0", "-1", "nan", "inf", "abc"])
def test_cli_invalid_hours(hours: str) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "members.thanhdat3010.w3.cli",
            "samples/tasks.csv",
            "--hours",
            hours,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "hours must be a positive number" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_date_changes_priority() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "members.thanhdat3010.w3.cli",
            "samples/tasks.csv",
            "--hours",
            "2",
            "--today",
            "2026-10-26",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout.index("Assignment") < result.stdout.index("DS exam")
    assert "1.5 h" in result.stdout and "0.5 h" in result.stdout
    assert result.stderr == ""


def test_bfs_personal_variant_six() -> None:
    """The instructor harness only supports variants 1-4; check BFS separately."""
    assert bfs({1: [2, 3], 2: [1, 4], 3: [4], 4: []}, 1) == [1, 2, 3, 4]
    assert bfs({}, None) == []
    assert bfs({}, "isolated") == ["isolated"]
