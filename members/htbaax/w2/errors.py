"""Custom exceptions and plan validation for Week 2 study planner."""

from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when required study hours exceed available capacity."""

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Plan needs {self.needed_h} hours, "
            f"but only {self.available_h} hours are available."
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Validate that total task effort does not exceed available hours.

    Raises:
        InfeasiblePlan: If total effort exceeds available_h.
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
