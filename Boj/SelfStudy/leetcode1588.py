def sumOddLengthSubarrays(arr):
        totSum=0

        for x in range(1,len(arr)+1,2):
            for i in range(len(arr)-x+1):
                totSum+=sum(arr[i:i+x])

        print(totSum)



arr=[1,4,2,5,3]
sumOddLengthSubarrays(arr)