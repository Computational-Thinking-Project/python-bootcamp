import sys
from pathlib import Path

# Ensure python-bootcamp is in sys.path
BOOTCAMP_DIR = Path(__file__).resolve().parents[2]
if str(BOOTCAMP_DIR) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP_DIR))

from members.benalexx007.w1.translate import selection_sort


def test_selection_sort_basic():
    arr = [64, 25, 12, 22, 11]
    result = selection_sort(arr)
    assert result == [11, 12, 22, 25, 64]
    # Check in-place mutation
    assert arr is result


def test_selection_sort_empty_and_single():
    assert selection_sort([]) == []
    assert selection_sort([42]) == [42]


def test_selection_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]


def test_selection_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]


def test_selection_sort_duplicates():
    arr = [3, 1, 2, 3, 1, 2]
    assert selection_sort(arr) == [1, 1, 2, 2, 3, 3]


def test_selection_sort_negative_numbers():
    arr = [-5, 3, 0, -2, 8, -10]
    assert selection_sort(arr) == [-10, -5, -2, 0, 3, 8]


def test_selection_sort_has_docstring():
    assert (
        selection_sort.__doc__ is not None and len(selection_sort.__doc__.strip()) > 0
    )
