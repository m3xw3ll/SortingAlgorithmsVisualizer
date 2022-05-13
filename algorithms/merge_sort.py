def merge_sort(a, start, end):
    """
    Function to recursively devide the array
    :param a: shuffled array
    :param start: startindex in array
    :param end: endindex in array
    :return: rearranged array
    """
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(a, start, mid)
    yield from merge_sort(a, mid + 1, end)
    yield from merge(a, start, mid, end)
    yield a


def merge(a, start, mid, end):
    """
    In-place Merge Sort
    :param a: shuffled array
    :param start: startindex in array
    :param mid: midindex in array
    :param end: endindex in array
    :return: rearranged array
    """
    merged = []
    left_idx = start
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= end:
        if a[left_idx] < a[right_idx]:
            merged.append(a[left_idx])
            left_idx += 1
        else:
            merged.append(a[right_idx])
            right_idx += 1

    while left_idx <= mid:
        merged.append(a[left_idx])
        left_idx += 1

    while right_idx <= end:
        merged.append(a[right_idx])
        right_idx += 1

    for i, sorted_val in enumerate(merged):
        a[start + i] = sorted_val
        yield a
