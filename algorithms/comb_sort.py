def calc_gap(gap):
    """
    Calculate new gap
    :param gap: previous gap
    :return: new gap
    """
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def comb_sort(a):
    """
    In-place Comb Sort
    :param a: shuffled array
    :return: rearranged array
    """
    gap = len(a)
    is_swaped = False

    while gap != 1 or is_swaped:
        gap = calc_gap(gap)
        is_swaped = False
        for i in range(0, len(a) - gap):
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
                is_swaped = True
                yield a
