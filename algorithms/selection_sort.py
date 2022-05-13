def selection_sort(a):
    """
    In-place Selection Sort
    :param a: shuffled array
    :return: rearranged array
    """
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

        yield a
