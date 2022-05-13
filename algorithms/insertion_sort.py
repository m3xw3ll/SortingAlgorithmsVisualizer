def insertion_sort(a):
    """
    In-place Intersection Sort
    :param a: shuffled array
    :return: rearranged array
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = key
        yield a
