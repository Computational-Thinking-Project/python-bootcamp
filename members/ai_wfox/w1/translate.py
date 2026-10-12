# Time: O(log(n + 1)); space: O(1), n = number of elements.
# a must be sorted ascending; duplicates return the first matching midpoint.


def binary_search(a: list[int], key: int) -> int:
    """Return a matching midpoint index in sorted a, or -1 if key is absent.

    Python's // computes an integer midpoint; / produces a float, whereas
    division of the nonnegative integer bounds in C++ produces an integer.
    Python integers also avoid fixed-width overflow when adding the bounds.
    """
    left_index, right_index = 0, len(a) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = a[middle_index]
        if middle_value == key:
            return middle_index
        if middle_value < key:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return -1
