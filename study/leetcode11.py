
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxItem = -1247000000
    firstIdx = 0
    lastIdx = 0
    for idx, item in enumerate(height):

        if item > maxItem:
            maxItem = item
            firstIdx = idx
        lastIdx = idx
    width = lastIdx - firstIdx
    height = height[lastIdx]

    return height * width


if __name__ == '__main__':
    #height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1,2,1]
    res = maxArea(height)
    print(res)
