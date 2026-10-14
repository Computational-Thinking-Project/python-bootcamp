"""Data contracts for the study planner module (Team T-W2).

Defines the shared Task and Block dataclasses used across the team modules.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a study task.

    Attributes:
        title: Description or name of the task.
        importance: Priority level, from 1 (lowest) to 5 (highest).
        effort_h: Estimated effort in hours.
        deadline: Due date for the task.
    """

    title: str
    importance: int  # 1-5
    effort_h: float
    deadline: date


@dataclass
class Block:
    """Represents a scheduled study block.

    Attributes:
        task: The task assigned to this block.
        hours: Number of hours allocated.
    """

    task: Task
    hours: float
