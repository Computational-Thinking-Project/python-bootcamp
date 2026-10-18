"""Custom exception and feasibility check for study planning (W2-3)."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Task


class InfeasiblePlan(Exception):
    """Raised when total required effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"InfeasiblePlan: {needed_h} hours needed exceeds {available_h} hours available"
        )

    def __str__(self) -> str:
        return f"InfeasiblePlan: {self.needed_h} hours needed exceeds {self.available_h} hours available"


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Validate that tasks can be completed within available hours.

    Raises InfeasiblePlan if total required effort exceeds available_h.
    """
    total_needed = sum(task.effort_h for task in tasks)
    if isinstance(total_needed, float) and total_needed.is_integer():
        needed: float | int = int(total_needed)
    else:
        needed = total_needed

    if needed > available_h:
        raise InfeasiblePlan(needed_h=needed, available_h=available_h)
