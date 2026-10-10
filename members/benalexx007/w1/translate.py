def selection_sort(arr: list[int]) -> list[int]:
    "Sort a list of integers in-place using selection sort and return the list."
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    """With this algorithm, one difference between Python and C++ verison is that Python relies
    on tuple packing/unpacking to swap elements (arr[i], arr[min_idx] = arr[min_idx], arr[i]) 
    without an explicit temporary variable, whereas C++ conventionally uses std::swap which 
    relies on move semantics (or a temporary variable)"""
    return arr
