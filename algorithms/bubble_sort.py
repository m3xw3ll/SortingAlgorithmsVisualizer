def bubble_sort(a):
    """
    In-place Bubble Sort
    :param a: shuffled array
    :return: rearranged array
    """
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
            yield a
