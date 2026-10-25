"""End-to-end tests for error handling and edge cases in the study planner CLI (Team T-W3)."""

import subprocess
import sys
from pathlib import Path

import pytest

from shared.study_planner.__main__ import main

REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLES_DIR = REPO_ROOT / "samples"
TASKS_CSV = SAMPLES_DIR / "tasks.csv"
TASKS_EMPTY = SAMPLES_DIR / "tasks_empty.csv"
TASKS_CORRUPTED = SAMPLES_DIR / "tasks_corrupted.csv"
TASKS_INFEASIBLE = SAMPLES_DIR / "tasks_infeasible.csv"


# ---------------------------------------------------------------------------
# CLI Subprocess Tests (Exit Codes, Output Streams & Graceful Exits)
# ---------------------------------------------------------------------------


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Execute the shared study planner CLI via subprocess and capture results."""
    return subprocess.run(
        [sys.executable, "-m", "shared.study_planner", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=15,
        check=False,
    )


def test_cli_missing_file_reports_error() -> None:
    """Non-existent CSV file must exit with code 1 and a descriptive stderr message."""
    missing_path = "non_existent_tasks_xyz.csv"
    res = run_cli(missing_path, "--hours", "2")

    assert res.returncode == 1
    assert res.stdout == ""
    assert "Tasks file not found" in res.stderr
    assert missing_path in res.stderr
    assert "Traceback" not in res.stderr


def test_cli_empty_file_reports_error() -> None:
    """Empty task file (0 bytes) must exit with code 1 and report empty file on stderr."""
    res = run_cli(str(TASKS_EMPTY), "--hours", "2")

    assert res.returncode == 1
    assert res.stdout == ""
    assert "File is empty" in res.stderr
    assert "Traceback" not in res.stderr


def test_cli_corrupted_csv_reports_error() -> None:
    """Malformed headers or invalid data columns must exit with code 2."""
    res = run_cli(str(TASKS_CORRUPTED), "--hours", "2")

    assert res.returncode == 2
    assert res.stdout == ""
    assert "Invalid CSV format" in res.stderr
    assert "Traceback" not in res.stderr


def test_cli_infeasible_plan_reports_error() -> None:
    """Task set exceeding available hours must exit with code 1 and mention InfeasiblePlan."""
    # tasks_infeasible.csv contains 250h total effort, exceeding available 20h
    res = run_cli(str(TASKS_INFEASIBLE), "--hours", "20")

    assert res.returncode == 1
    assert res.stdout == ""
    assert "InfeasiblePlan" in res.stderr
    assert "250 hours needed exceeds 20 hours available" in res.stderr
    assert "Traceback" not in res.stderr


@pytest.mark.parametrize("invalid_hours", ["-1", "0", "-0.5", "abc", "NaN", "inf"])
def test_cli_invalid_hours_reports_usage_error(invalid_hours: str) -> None:
    """Non-positive or non-finite study hours must exit with code 2."""
    res = run_cli(str(TASKS_CSV), "--hours", invalid_hours)

    assert res.returncode == 2
    assert res.stdout == ""
    assert "hours must be a positive number" in res.stderr
    assert "Traceback" not in res.stderr


def test_cli_invalid_today_date_reports_error() -> None:
    """Malformed --today date format must exit with code 2 and descriptive stderr."""
    res = run_cli(str(TASKS_CSV), "--hours", "2", "--today", "26-10-2026")

    assert res.returncode == 2
    assert res.stdout == ""
    assert "today must be a valid date in YYYY-MM-DD format" in res.stderr
    assert "Traceback" not in res.stderr


# ---------------------------------------------------------------------------
# Direct main() Function Tests (Capsys Fixture Verification)
# ---------------------------------------------------------------------------


def test_main_missing_file_direct(capsys: pytest.CaptureFixture[str]) -> None:
    """Directly invoking main() with missing file returns 1 and prints to stderr."""
    exit_code = main(["nonexistent.csv", "--hours", "2"])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert "Tasks file not found" in captured.err


def test_main_empty_file_direct(capsys: pytest.CaptureFixture[str]) -> None:
    """Directly invoking main() with empty file returns 1 and prints to stderr."""
    exit_code = main([str(TASKS_EMPTY), "--hours", "2"])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert "File is empty" in captured.err


def test_main_corrupted_csv_direct(capsys: pytest.CaptureFixture[str]) -> None:
    """Directly invoking main() with corrupted CSV returns 2 and prints to stderr."""
    exit_code = main([str(TASKS_CORRUPTED), "--hours", "2"])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert captured.out == ""
    assert "Invalid CSV format" in captured.err


def test_main_infeasible_plan_direct(capsys: pytest.CaptureFixture[str]) -> None:
    """Directly invoking main() with infeasible workload returns 1 and reports InfeasiblePlan."""
    exit_code = main([str(TASKS_INFEASIBLE), "--hours", "10"])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert "InfeasiblePlan" in captured.err


@pytest.mark.parametrize("invalid_hours", ["-2", "0", "xyz"])
def test_main_invalid_hours_direct(
    invalid_hours: str, capsys: pytest.CaptureFixture[str]
) -> None:
    """Directly invoking main() with invalid hours returns 2."""
    exit_code = main([str(TASKS_CSV), "--hours", invalid_hours])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert captured.out == ""
    assert "hours must be a positive number" in captured.err


def test_main_invalid_today_direct(capsys: pytest.CaptureFixture[str]) -> None:
    """Directly invoking main() with invalid date returns 2."""
    exit_code = main([str(TASKS_CSV), "--hours", "2", "--today", "bad-date"])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert captured.out == ""
    assert "today must be a valid date in YYYY-MM-DD format" in captured.err
