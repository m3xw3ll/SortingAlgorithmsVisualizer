def shell_sort(a):
    """
    In-place Shell Sort
    :param a: shuffled array
    :return: rearranged array
    """
    split = len(a) // 2
    while split > 0:
        for i in range(split, len(a)):
            tmp = a[i]
            j = i
            while j >= split and a[j - split] > tmp:
                a[j] = a[j - split]
                yield a
                j -= split
            a[j] = tmp
            yield a
        split = split // 2
        yield a