"""W2-3: checking total effort uses O(n) time and O(1) auxiliary space."""

from math import isfinite

from .models import Task


class InfeasiblePlan(Exception):
    """Carry the required and available hours for an infeasible plan."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        return f"Plan needs {self.needed_h:g} h, but only {self.available_h:g} h are available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the sum of effort exceeds available hours."""
    if not isfinite(available_h) or available_h < 0:
        raise ValueError("available_h must be finite and nonnegative")
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
