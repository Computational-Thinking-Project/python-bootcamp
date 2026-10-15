from dataclasses import dataclass
from .models import Task

class InfeasiblePlan(Exception):
    needed_h: float
    available_h: float
    
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
    
    def __str__(self) -> str:
        return f"Need {self.needed_h} hours, {self.available_h} hours available."

def check_feasible(tasks: list[Task], available_h: float):
    total_effort = sum(task.effort_h for task in tasks)
    if total_effort > available_h:
        raise InfeasiblePlan(total_effort, available_h)
        