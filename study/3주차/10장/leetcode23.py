def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def mergeKLists(lists):
    stack = []
    for i in lists:
        for j in i:
            stack.append(j)

    print(stack)
    res = bubble_sort(stack)
    print(res)




if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    mergeKLists(lists)