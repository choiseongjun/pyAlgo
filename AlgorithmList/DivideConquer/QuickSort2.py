def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr

S = [15, 22, 13, 27, 12, 10, 20, 25]
print('Before=', S)

print('After=', quick_sorted(S))