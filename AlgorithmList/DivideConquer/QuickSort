def quickSort(S, low, high):
    if (high > low):
        mid = partition(S, low, high)
        quickSort(S, low, mid)
        quickSort(S, mid + 1, high)


def partition(S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        print(i, j, S)
        if (S[i] < pivotitem):
            j += 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint


S = [15, 22, 13, 27, 12, 10, 20, 25]
print('Before=', S)
quickSort(S, 0, len(S) - 1)
print('After=', S)
