def transpose(matrix: list[list[int]]) -> list[list[int]]:
    " Unlike C++, Python uses dynamic lists instead of explicitly typed vector<vector<int>> "

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    transposeMatrix = []

    for col in range(cols):
        newRow = []
        for row in range(rows):
            newRow.append(matrix[row][col])
        transposeMatrix.append(newRow)

    return transposeMatrix
