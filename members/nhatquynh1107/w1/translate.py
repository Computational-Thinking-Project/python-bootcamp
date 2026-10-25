"""Translate the C++ matrix transpose exercise into Python."""


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a rectangular matrix, returning [] for an empty input.

    Unlike C++, Python uses dynamic lists instead of explicitly typed vectors.
    """

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    transposeMatrix: list[list[int]] = []

    for col in range(cols):
        newRow: list[int] = []
        for row in range(rows):
            newRow.append(matrix[row][col])
        transposeMatrix.append(newRow)

    return transposeMatrix
