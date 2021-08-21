from sys import stdin

def solution(nums):
    stack = []
    result = [-1 for _ in range(N)]

    stack.append(0)
    i=1

    while stack and i<N:
        while stack and nums[stack[-1]] <nums[i]:
            result[stack[-1]] = nums[i]
            stack.pop()

        stack.append(i)
        i+=1
    for i in result:
        print(i,end = ' ')



if __name__ == '__main__':
    N = int(input())
    nums = list(map(int,input().split()))
    solution(nums)