#실패코드
def solution(strings, n):
    answer = []
    lenstr=len(strings)
    for i in range(lenstr):
        for j in range(lenstr):
            if i<=j:
                if strings[i][n]>strings[j][n]:
                    tmp=strings[i]
                    strings[i]=strings[j]
                    strings[j]=tmp

    answer=strings
    return answer

string=["abce", "abcd", "cdx"]
n=1
a=solution(string,n)
print(a)
