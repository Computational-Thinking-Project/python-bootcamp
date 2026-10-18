"""Tests for shared/study_planner/prioritise.py (Team T-W2)."""

from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise


def test_higher_priority_task_comes_first():
    today = date(2026, 10, 17)
    tasks = [
        Task("Task A", 4, 2.0, date(2026, 10, 19)),
        Task("Task B", 5, 3.0, date(2026, 10, 22)),
    ]

    result = prioritise(tasks, today)

    assert [task.title for task in result] == ["Task A", "Task B"]


def test_empty_task_list():
    assert prioritise([], date(2026, 10, 17)) == []


def test_task_due_today():
    today = date(2026, 10, 17)
    tasks = [
        Task("Future task", 5, 2.0, date(2026, 10, 19)),
        Task("Due today", 4, 1.0, today),
    ]

    result = prioritise(tasks, today)

    assert [task.title for task in result] == [
        "Due today",
        "Future task",
    ]


def test_overdue_task_uses_one_day():
    today = date(2026, 10, 17)
    tasks = [
        Task("Future task", 5, 2.0, date(2026, 10, 19)),
        Task("Overdue task", 3, 1.0, date(2026, 10, 15)),
    ]

    result = prioritise(tasks, today)

    assert [task.title for task in result] == [
        "Overdue task",
        "Future task",
    ]


def test_equal_priority_keeps_original_order():
    today = date(2026, 10, 17)
    tasks = [
        Task("Task B", 2, 1.0, today),
        Task("Task A", 4, 2.0, date(2026, 10, 19)),
    ]

    result = prioritise(tasks, today)

    assert [task.title for task in result] == [
        "Task B",
        "Task A",
    ]


def test_original_task_order_is_unchanged():
    today = date(2026, 10, 17)
    tasks = [
        Task("Task B", 5, 2.0, date(2026, 10, 22)),
        Task("Task A", 4, 2.0, date(2026, 10, 19)),
    ]

    prioritise(tasks, today)

    assert [task.title for task in tasks] == ["Task B", "Task A"]


def test_same_score_keeps_original_order():
    today = date(2026, 10, 17)
    tasks = [
        Task("Task A", 2, 1.0, date(2026, 10, 19)),
        Task("Task B", 4, 2.0, date(2026, 10, 21)),
    ]

    result = prioritise(tasks, today)

    assert [task.title for task in result] == ["Task A", "Task B"]
