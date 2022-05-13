def cocktail_sort(A, start, end):
    swap = True
    while swap:
        for i in range(start, end):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swap = True
                yield A

        if swap == False:
            break

        swap = False

        for j in range(end-1, start-1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
                yield A

        start += 1
