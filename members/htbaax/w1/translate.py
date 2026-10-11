
def insertion_sort(a: list[int]) -> list[int]:
    """Sort a list in place using insertion sort.

    Unlike C++ vectors, Python lists do not enforce a single element
    type at runtime; the list[int] annotation is only a type hint."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


