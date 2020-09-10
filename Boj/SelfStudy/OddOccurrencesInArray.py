def solution(A):
    idxs = []
    for idx, item in enumerate(A):
        if idx in idxs:
            continue
        elif item in A[idx + 1:]:
            idxs.append(idx)
            idxs.append(A[idx + 1:].index(item) + idx + 1)
        else:
            return item

A=[9,3,9,3,9,7,9]
print(solution(A))