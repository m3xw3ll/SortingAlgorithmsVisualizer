def gnome_sort(a):
    """
    In-place Gnome Sort
    :param a: shuffled array
    :return: rearranged array
    """
    idx = 0
    while idx < len(a):
        if idx == 0:
            idx += 1
        if a[idx] >= a[idx-1]:
            idx += 1
        else:
            a[idx], a[idx-1] = a[idx-1], a[idx]
            idx -= 1
            yield a