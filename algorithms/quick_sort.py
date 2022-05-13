def quick_sort(a, left, right):
    """
    In-place Quick Sort
    :param a: shuffled array
    :param left: leftmost element in array
    :param right: rightmost element in array
    :return: rearranged array
    """
    if left >= right:
        return
    x = a[left]
    j = left
    for i in range(left + 1, right + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[left], a[j] = a[j], a[left]
    yield a

    yield from quick_sort(a, left, j - 1)
    yield from quick_sort(a, j + 1, right)
