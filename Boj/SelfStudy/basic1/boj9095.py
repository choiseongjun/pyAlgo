from sys import stdin

def solution(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return solution(n-1)+solution(n-2)+solution(n-3)

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        res = solution(int(stdin.readline()))
        print(res)