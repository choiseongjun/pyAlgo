def trap(height):
    if not height:
        return 0

    volunm = 0
    left=0
    right = len(height) - 1
    left_max, right_max = height[left], height[right]


    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        print(left_max,right_max)
        if left_max <= right_max:
            volunm += left_max - height[left]
            left += 1
        else:
            volunm += right_max - height[right]
            right -= 1
    return volunm


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
a = trap(height)
print(a)
