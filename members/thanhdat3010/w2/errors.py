"""Custom exception and feasibility checks for study plans."""

from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when required study effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Plan is infeasible: {needed_h} hours needed, but only {available_h} hours available."
        )

    def __str__(self) -> str:
        return f"InfeasiblePlan: {self.needed_h} hours needed exceeds {self.available_h} hours available"


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Validate that tasks can be completed within available hours.

    Raises:
        InfeasiblePlan: If total effort required exceeds available_h.
    """
    total_needed = sum(task.effort_h for task in tasks)
    if isinstance(total_needed, float) and total_needed.is_integer():
        needed: float | int = int(total_needed)
    else:
        needed = total_needed

    if needed > available_h:
        raise InfeasiblePlan(needed_h=needed, available_h=available_h)
