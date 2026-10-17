"""T-W2: verify readable plans using the shared Task and Block contracts.

Rendering n blocks into L output characters takes O(n + L) time and space.
Assertions check visible content without prescribing line punctuation.
"""

import re
from copy import deepcopy
from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.render import render


def make_block(title: str, hours: float = 1.25) -> Block:
    """Distinguish allocated hours from the task's total estimated effort."""
    return Block(Task(title, 3, 9.0, date(2026, 10, 30)), hours)


def test_empty_plan_returns_text() -> None:
    assert isinstance(render([]), str)


@pytest.mark.parametrize("hours,display", [(0.5, "0.5"), (1.25, "1.25"), (2.0, "2")])
def test_single_block_shows_title_and_allocated_hours(
    hours: float, display: str
) -> None:
    result = render([make_block("Python practice", hours)])
    assert isinstance(result, str)
    assert "Python practice" in result
    assert re.search(r"(?<![\d.])" + re.escape(display) + r"(?:\.0+)?\s*h\b", result)


def test_multiple_blocks_preserve_input_order() -> None:
    result = render(
        [make_block("Zebra review", 1.0), make_block("Alpha practice", 2.0)]
    )
    assert result.index("Zebra review") < result.index("Alpha practice")


def test_unicode_and_punctuation_in_title_are_preserved() -> None:
    title = "Ôn tập Python, chapter 2: files & classes"
    assert title in render([make_block(title)])


def test_duplicate_blocks_remain_visible() -> None:
    block = make_block("Repeat practice", 0.5)
    assert render([block, block]).count("Repeat practice") == 2


def test_render_does_not_modify_the_plan() -> None:
    blocks = [make_block("Practice", 0.5), make_block("Review", 2.0)]
    original = deepcopy(blocks)
    render(blocks)
    assert blocks == original
