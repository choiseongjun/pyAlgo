def sortArrayByParity(A):
    i = 0
    for j in range(len(A)):
        if A[j] % 2 == 0:
            print(A[i])
            A[i], A[j] = A[j], A[i]
            i += 1
    print(A)
    return A

arr=[3,1,2,4]
sortArrayByParity((arr))