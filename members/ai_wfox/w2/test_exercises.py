"""Supplementary W2 tests for invalid rows, boundaries, Unicode, and CLI use."""

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from .errors import InfeasiblePlan, check_feasible
from .io_utils import load_tasks, save_json
from .models import Task

ROOT = Path(__file__).resolve().parents[3]
HEADER = "title,importance,effort_h,deadline\n"


@pytest.mark.parametrize(
    "today,expected",
    [(date(2024, 2, 28), 2), (date(2024, 3, 1), 0), (date(2024, 3, 2), 0)],
)
def test_days_left_handles_leap_day_and_deadline(today: date, expected: int) -> None:
    assert Task("exam", 5, 1, date(2024, 3, 1)).days_left(today) == expected


@pytest.mark.parametrize(
    "row",
    [
        "bad,9,1,2026-10-30",
        "bad,2,-1,2026-10-30",
        "bad,2,nan,2026-10-30",
        "bad,2,1,2026-02-30",
        "bad,2,1",
        "bad,2,1,2026-10-30,extra",
        ",2,1,2026-10-30",
    ],
)
def test_invalid_second_row_reports_line_three(tmp_path: Path, row: str) -> None:
    path = tmp_path / "bad.csv"
    path.write_text(HEADER + "ok,2,1,2026-10-30\n" + row + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(path)


def test_csv_quotes_unicode_and_json_dates(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"
    path.write_text(HEADER + '"Ôn tập, Python",4,1.25,2026-10-30\n', encoding="utf-8")
    tasks = load_tasks(path)
    out = tmp_path / "tasks.json"
    save_json(tasks, out)
    assert json.loads(out.read_text(encoding="utf-8")) == [
        {
            "title": "Ôn tập, Python",
            "importance": 4,
            "effort_h": 1.25,
            "deadline": "2026-10-30",
        }
    ]


def test_header_only_input_and_empty_json(tmp_path: Path) -> None:
    path = tmp_path / "empty.csv"
    path.write_text(HEADER, encoding="utf-8")
    assert load_tasks(path) == []
    out = tmp_path / "empty.json"
    save_json([], out)
    assert json.loads(out.read_text(encoding="utf-8")) == []


def test_feasibility_boundary_and_exception_details() -> None:
    tasks = [Task("exam", 5, 2, date(2026, 10, 30))]
    check_feasible(tasks, 2)
    check_feasible([], 0)
    with pytest.raises(InfeasiblePlan) as exc:
        check_feasible(tasks, 1)
    assert (exc.value.needed_h, exc.value.available_h) == (2, 1)
    assert "2 h" in str(exc.value) and "1 h" in str(exc.value)


def test_package_entry_point_loads_sample() -> None:
    run = subprocess.run(
        [sys.executable, "-m", "members.ai_wfox.w2"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert run.returncode == 0, run.stderr
    assert "DS exam" in run.stdout and "Assignment" in run.stdout


@pytest.mark.parametrize(
    "header", ["", "wrong,columns\n", "title,importance,effort_h,title\n"]
)
def test_invalid_header_reports_line_one(tmp_path: Path, header: str) -> None:
    path = tmp_path / "header.csv"
    path.write_text(header, encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_tasks(path)


def test_malformed_csv_reports_parser_line(tmp_path: Path) -> None:
    path = tmp_path / "malformed.csv"
    path.write_text(
        HEADER + "ok,2,1,2026-10-30\n" + '"unfinished,2,1,2026-10-30\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(path)
