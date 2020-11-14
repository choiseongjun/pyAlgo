def findDuplicates(nums):
    for i in range(len(nums)):
        nums[abs(nums[i])-1]*=-1
        print(nums[abs(nums[i])-1])

nums=[4,3,2,7,8,2,3,1]
findDuplicates(nums)