
#나중에 다시 보기
def nextGreaterElement(nums1, nums2):

    seen={}

    for i,v in enumerate(nums2):
        seen[v]=i

    result=[]
    for v in nums1:
        found=False
        # print(seen[v])
        for j in range(seen[v],len(nums2)):
            print(j)
            if v<nums2[j]:
                result.append(nums2[j])
                found = True
                break

        if not found:
            result.append(-1)
    return result


if __name__ == '__main__':
    nums1=[4,1,2]
    nums2=[1,3,4,2]
    res = nextGreaterElement(nums1,nums2)
    print(res)