"""Task validation and date arithmetic: O(1) time and space."""

from dataclasses import dataclass
from datetime import date
from math import isfinite


@dataclass
class Task:
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
        return max(0, (self.deadline - today).days)
