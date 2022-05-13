def count_sort(a):
    maxElement= max(a)
    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength

    for el in a:
        countArray[el] += 1
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    outputArray = [0] * len(a)
    i = len(a) - 1

    while i >= 0:
        currentEl = a[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1
        yield outputArray
