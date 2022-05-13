def odd_even_sort(a):
    """
    In-place Odd Even Sort
    :param a: shuffled array
    :return: rearranged array
    """
    is_sorted = 0
    while is_sorted == 0:
        is_sorted = 1
        for i in range(1, len(a) - 1, 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_sorted = 0
                yield a

        for i in range(0, len(a) - 1, 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_sorted = 0
                yield a
