"""W2-1: Task construction and days_left use O(1) time and space."""

from dataclasses import dataclass
from datetime import date
from math import isfinite


@dataclass
class Task:
    """A task with importance 1-5, finite nonnegative effort, and a deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
        if not isfinite(self.effort_h) or self.effort_h < 0:
            raise ValueError("effort_h must be finite and nonnegative")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, clamped to zero after it passes."""
        return max(0, (self.deadline - today).days)
