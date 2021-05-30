def intersection(nums1, nums2):
    res1 = set(nums1)
    res2 = set(nums2)

    reply = res1.intersection(res2)

    answer= []
    for i in reply:
        answer.append(i)
    return answer


if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = intersection(nums1,nums2)
