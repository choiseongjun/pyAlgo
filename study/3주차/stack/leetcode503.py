def nextGreaterElements(nums):
    ans = [-1] * len(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j]>nums[i]:
                ans[i]=nums[j]
                break


    return ans



if __name__ == '__main__':
    nums = [1,5,3,6,8]
    res = nextGreaterElements(nums)
    print(res)