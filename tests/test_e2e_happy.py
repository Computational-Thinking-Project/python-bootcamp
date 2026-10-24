"""Happy-path E2E tests for the shared study planner CLI (Team T-W3)."""

import re
import subprocess
import sys
from pathlib import Path

import pytest

from shared.study_planner.__main__ import main

REPO_ROOT = Path(__file__).resolve().parents[1]
TASKS_CSV = REPO_ROOT / "samples" / "tasks.csv"
TODAY = "2026-10-26"


def assert_plan(output: str, expected: list[tuple[str, float]]) -> None:
    """Check task order and allocated hours without fixing separator style."""
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    assert len(lines) == len(expected)

    for line, (title, hours) in zip(lines, expected):
        assert title in line
        match = re.search(r"(?<![\d.])(\d+(?:\.\d+)?)\s*h\s*$", line)
        assert match is not None, f"Missing allocated hours in: {line}"
        assert float(match.group(1)) == pytest.approx(hours)


def test_cli_module_runs_successfully() -> None:
    """Run the real module with the active Python interpreter and sample CSV."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            str(TASKS_CSV),
            "--hours",
            "2",
            "--today",
            TODAY,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=15,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert_plan(result.stdout, [("Assignment", 1.5), ("DS exam", 0.5)])


@pytest.mark.parametrize(
    "hours,expected",
    [
        ("2", [("Assignment", 1.5), ("DS exam", 0.5)]),
        ("3", [("Assignment", 1.5), ("DS exam", 1.5)]),
        ("1.5", [("Assignment", 1.5)]),
    ],
)
def test_main_allocates_requested_hours(
    hours: str,
    expected: list[tuple[str, float]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Accept integer and decimal budgets and capture a successful plan."""
    result = main([str(TASKS_CSV), "--hours", hours, "--today", TODAY])
    captured = capsys.readouterr()

    assert result == 0
    assert captured.err == ""
    assert_plan(captured.out, expected)


def test_output_file_contains_expected_plan(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """Save the plan to a UTF-8 file without printing it to the terminal."""
    output_file = tmp_path / "plan.txt"
    result = main(
        [
            str(TASKS_CSV),
            "--hours",
            "2",
            "--today",
            TODAY,
            "--output",
            str(output_file),
        ]
    )
    captured = capsys.readouterr()

    assert result == 0
    assert captured.out == captured.err == ""
    assert output_file.is_file()
    assert_plan(
        output_file.read_text(encoding="utf-8"),
        [("Assignment", 1.5), ("DS exam", 0.5)],
    )
