"""Tests for shared/study_planner/parse.py (Team T-W2)."""

from datetime import date
from pathlib import Path

import pytest

from shared.contract import Task
from shared.study_planner.parse import parse_csv

SAMPLES = Path(__file__).resolve().parents[1] / "samples"


def test_parse_csv_sample() -> None:
    """Test parsing standard sample tasks CSV."""
    tasks = parse_csv(SAMPLES / "tasks.csv")
    assert len(tasks) >= 2

    task1 = tasks[0]
    assert isinstance(task1, Task)
    assert task1.title == "DS exam"
    assert task1.importance == 5
    assert task1.effort_h == 6.0
    assert task1.deadline == date(2026, 10, 30)

    task2 = tasks[1]
    assert isinstance(task2, Task)
    assert task2.title == "Assignment"
    assert task2.importance == 4
    assert task2.effort_h == 1.5
    assert task2.deadline == date(2026, 10, 27)


def test_parse_csv_string_path() -> None:
    """Test passing string path instead of Path object."""
    tasks = parse_csv(str(SAMPLES / "tasks.csv"))
    assert len(tasks) >= 2


def test_parse_csv_missing_file() -> None:
    """Test that a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        parse_csv("non_existent_file.csv")


def test_parse_csv_empty_file(tmp_path: Path) -> None:
    """Test that an empty file returns an empty list."""
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("", encoding="utf-8")
    assert parse_csv(empty_csv) == []


def test_parse_csv_header_only(tmp_path: Path) -> None:
    """Test that a CSV with only the header row returns an empty list."""
    header_only = tmp_path / "header_only.csv"
    header_only.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    assert parse_csv(header_only) == []


def test_parse_csv_invalid_header(tmp_path: Path) -> None:
    """Test that an incorrect header raises ValueError with line 1."""
    bad_header = tmp_path / "bad_header.csv"
    bad_header.write_text("name,priority,effort,due_date\nDS exam,5,6,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        parse_csv(bad_header)


def test_parse_csv_invalid_column_count(tmp_path: Path) -> None:
    """Test that rows with missing or extra columns raise ValueError with line number."""
    bad_row = tmp_path / "bad_row.csv"
    bad_row.write_text("title,importance,effort_h,deadline\nDS exam,5,6\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(bad_row)


def test_parse_csv_invalid_importance_non_int(tmp_path: Path) -> None:
    """Test that non-integer importance raises ValueError."""
    bad_importance = tmp_path / "bad_importance.csv"
    bad_importance.write_text("title,importance,effort_h,deadline\nTask,high,2.0,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(bad_importance)


def test_parse_csv_invalid_importance_range(tmp_path: Path) -> None:
    """Test that importance out of 1-5 range raises ValueError."""
    for bad_val in [0, 6, -1, 10]:
        bad_csv = tmp_path / f"bad_importance_{bad_val}.csv"
        bad_csv.write_text(f"title,importance,effort_h,deadline\nTask,{bad_val},2.0,2026-10-30\n", encoding="utf-8")
        with pytest.raises(ValueError, match="line 2"):
            parse_csv(bad_csv)


def test_parse_csv_invalid_effort_negative(tmp_path: Path) -> None:
    """Test that negative effort raises ValueError."""
    bad_effort = tmp_path / "bad_effort.csv"
    bad_effort.write_text("title,importance,effort_h,deadline\nTask,3,-1.0,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(bad_effort)


def test_parse_csv_invalid_date_format(tmp_path: Path) -> None:
    """Test that non-ISO date string raises ValueError."""
    bad_date = tmp_path / "bad_date.csv"
    bad_date.write_text("title,importance,effort_h,deadline\nTask,3,1.0,30-10-2026\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(bad_date)


def test_parse_csv_empty_title(tmp_path: Path) -> None:
    """Test that blank/empty title raises ValueError."""
    bad_title = tmp_path / "bad_title.csv"
    bad_title.write_text("title,importance,effort_h,deadline\n   ,3,1.0,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(bad_title)


def test_parse_csv_whitespace_and_blank_lines(tmp_path: Path) -> None:
    """Test that whitespace is trimmed and blank lines are ignored."""
    csv_content = """title,importance,effort_h,deadline

   Task A  ,  3  ,  2.5  ,  2026-11-01   

   Task B  ,  1  ,  0.5  ,  2026-11-02   
"""
    clean_csv = tmp_path / "whitespace.csv"
    clean_csv.write_text(csv_content, encoding="utf-8")
    tasks = parse_csv(clean_csv)
    assert len(tasks) >= 2
    assert tasks[0].title == "Task A"
    assert tasks[0].importance == 3
    assert tasks[0].effort_h == 2.5
    assert tasks[0].deadline == date(2026, 11, 1)
    assert tasks[1].title == "Task B"
    assert tasks[1].importance == 1
    assert tasks[1].effort_h == 0.5
    assert tasks[1].deadline == date(2026, 11, 2)
