from members.nhatquynh1107.w1.translate import transpose
from members.nhatquynh1107.w1.grades import summary
from members.nhatquynh1107.w1.rules import can_register_thesis, missing


def test_transpose_square_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert transpose(matrix) == expected


def test_transpose_rectangular_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    expected = [
        [1, 5],
        [2, 6],
        [3, 7],
        [4, 8]
    ]
    assert transpose(matrix) == expected


def test_transpose_single_row_and_single_column():
    assert transpose([[10, 20, 30]]) == [[10], [20], [30]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


def test_transpose_empty_matrix_edge_case():
    assert transpose([]) == []


def test_grades_summary_and_thesis_rules():
    res = summary([5.0, 7.5, 9.0])
    assert res["min"] == 5.0 and res["max"] == 9.0
    assert res["mean"] == 7.17 and res["median"] == 7.5

    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(110, 1.8) is False
    assert len(missing(110, 1.8)) == 2
