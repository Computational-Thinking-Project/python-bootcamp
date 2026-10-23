"""Dat's T-W3 output/verbose acceptance tests (Issue #45)."""

from pathlib import Path

import pytest

from shared.study_planner.__main__ import main
from shared.study_planner.render import render_summary


@pytest.fixture
def tasks_csv(tmp_path: Path) -> Path:
    """Use a feasible fixture, independent of team sample changes."""
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "Ôn Python,4,1.5,2026-10-27\nReview,3,0.25,2026-10-28\n",
        encoding="utf-8",
    )
    return path


@pytest.mark.parametrize("flag", ["-o", "--output"])
def test_output_matches_standard_render(
    tasks_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str], flag: str
) -> None:
    args = [str(tasks_csv), "--hours", "2", "--today", "2026-10-26"]
    assert main(args) == 0
    expected = capsys.readouterr().out
    output = tmp_path / "kết quả.txt"
    assert main([*args, flag, str(output)]) == 0
    assert output.read_text(encoding="utf-8") == expected
    captured = capsys.readouterr()
    assert captured.out == captured.err == ""


@pytest.mark.parametrize("flag", ["-v", "--verbose"])
def test_verbose_file_and_terminal_summary(
    tasks_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str], flag: str
) -> None:
    output = tmp_path / "plan.txt"
    assert main([str(tasks_csv), "--hours", "2", "-o", str(output), flag]) == 0
    captured = capsys.readouterr()
    assert "Tasks selected: 2" in captured.out
    assert "Remaining hours: 0.25 h" in captured.out
    assert "Allocated hours: 1.75 h" in captured.out
    content = output.read_text(encoding="utf-8")
    assert "Ôn Python" in content and captured.out.strip() in content
    assert captured.err == ""


def test_verbose_without_output(
    tasks_csv: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert main([str(tasks_csv), "--hours", "2", "-v"]) == 0
    result = capsys.readouterr()
    assert "Ôn Python" in result.out and "Tasks selected: 2" in result.out
    assert result.err == ""


def test_write_error_and_source_protection(
    tasks_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    original = tasks_csv.read_bytes()
    assert main([str(tasks_csv), "--hours", "2", "-o", str(tasks_csv)]) == 1
    assert "must differ" in capsys.readouterr().err
    assert tasks_csv.read_bytes() == original
    assert main([str(tasks_csv), "--hours", "2", "-o", str(tmp_path)]) == 1
    assert "Cannot write output file" in capsys.readouterr().err


def test_empty_summary() -> None:
    assert render_summary([], 2, 2) == (
        "Tasks selected: 0\nAvailable hours: 2 h\n"
        "Allocated hours: 0 h\nRemaining hours: 2 h"
    )
