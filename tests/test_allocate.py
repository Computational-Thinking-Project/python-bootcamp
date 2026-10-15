"""Unit tests for shared/study_planner/allocate.py (Team T-W2).

Tests greedy study time allocation across prioritized tasks.
"""

from __future__ import annotations

from datetime import date

import pytest
from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def test_allocate_sample_tasks() -> None:
    """Test greedy allocation on sample tasks matching the course tutorial."""
    task1 = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    task2 = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    tasks = [task1, task2]

    blocks = allocate(tasks, 2.0)

    assert len(blocks) == 2
    assert blocks[0].task == task1
    assert blocks[0].hours == 1.5
    assert blocks[1].task == task2
    assert blocks[1].hours == 0.5
    assert sum(b.hours for b in blocks) == 2.0


def test_allocate_exact_hours() -> None:
    """Test allocation when available hours match total task effort exactly."""
    task1 = Task("Math homework", 3, 2.0, date(2026, 11, 1))
    task2 = Task("Physics lab", 4, 3.0, date(2026, 11, 2))
    tasks = [task1, task2]

    blocks = allocate(tasks, 5.0)

    assert len(blocks) == 2
    assert blocks[0].hours == 2.0
    assert blocks[1].hours == 3.0
    assert sum(b.hours for b in blocks) == 5.0


def test_allocate_surplus_hours() -> None:
    """Test allocation when available hours exceed total required effort."""
    task1 = Task("Essay outline", 2, 1.0, date(2026, 11, 5))
    task2 = Task("Reading chapter", 3, 2.5, date(2026, 11, 6))
    tasks = [task1, task2]

    blocks = allocate(tasks, 10.0)

    # Should only allocate up to needed effort, no extra hours given
    assert len(blocks) == 2
    assert blocks[0].hours == 1.0
    assert blocks[1].hours == 2.5
    assert sum(b.hours for b in blocks) == 3.5


def test_allocate_partial_first_task() -> None:
    """Test when available hours are less than the effort of the first task."""
    task1 = Task("Big project", 5, 4.0, date(2026, 10, 28))
    task2 = Task("Small quiz", 3, 1.0, date(2026, 10, 29))
    tasks = [task1, task2]

    blocks = allocate(tasks, 1.5)

    assert len(blocks) == 1
    assert blocks[0].task == task1
    assert blocks[0].hours == 1.5


def test_allocate_zero_available_hours() -> None:
    """Test that zero available hours produces no blocks."""
    task = Task("Any task", 3, 2.0, date(2026, 11, 1))
    blocks = allocate([task], 0.0)
    assert blocks == []


def test_allocate_negative_hours_raises_error() -> None:
    """Test that negative available hours raises a ValueError."""
    task = Task("Any task", 3, 2.0, date(2026, 11, 1))
    with pytest.raises(ValueError, match="non-negative"):
        allocate([task], -1.0)


def test_allocate_empty_tasks_list() -> None:
    """Test that an empty task list produces an empty block list."""
    blocks = allocate([], 4.0)
    assert blocks == []


def test_allocate_preserves_task_order() -> None:
    """Test that greedy allocation respects the input task ordering."""
    task1 = Task("First priority", 5, 1.0, date(2026, 11, 1))
    task2 = Task("Second priority", 4, 1.0, date(2026, 11, 2))
    task3 = Task("Third priority", 3, 1.0, date(2026, 11, 3))
    tasks = [task1, task2, task3]

    blocks = allocate(tasks, 2.5)

    assert len(blocks) == 3
    assert blocks[0].task == task1
    assert blocks[0].hours == 1.0
    assert blocks[1].task == task2
    assert blocks[1].hours == 1.0
    assert blocks[2].task == task3
    assert blocks[2].hours == 0.5


def test_allocate_fractional_hours() -> None:
    """Test handling of decimal and fractional effort values."""
    task1 = Task("Task A", 3, 0.75, date(2026, 11, 1))
    task2 = Task("Task B", 3, 0.5, date(2026, 11, 2))
    tasks = [task1, task2]

    blocks = allocate(tasks, 1.0)

    assert len(blocks) == 2
    assert blocks[0].hours == 0.75
    assert blocks[1].hours == 0.25
    assert sum(b.hours for b in blocks) == 1.0


def test_allocate_does_not_mutate_input() -> None:
    """Test that allocate does not modify the input task list or task objects."""
    task1 = Task("Task 1", 4, 2.0, date(2026, 11, 1))
    task2 = Task("Task 2", 3, 3.0, date(2026, 11, 2))
    tasks = [task1, task2]
    original_len = len(tasks)

    allocate(tasks, 3.0)

    assert len(tasks) == original_len
    assert task1.effort_h == 2.0
    assert task2.effort_h == 3.0


def test_allocate_returns_block_instances() -> None:
    """Test that return values strictly adhere to the Block contract."""
    task = Task("Task", 3, 2.0, date(2026, 11, 1))
    blocks = allocate([task], 2.0)

    assert len(blocks) == 1
    block = blocks[0]
    assert isinstance(block, Block)
    assert isinstance(block.task, Task)
    assert isinstance(block.hours, (int, float))
    assert block.hours > 0
