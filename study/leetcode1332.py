def removePalindromeSub(s):

    cnt = 0
    palin_check = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            cnt=0
            palin_check =False


        if palin_check:
            cnt=1
        else:
            cnt=1
            cnt+=1

    print(cnt)
    return cnt
    # for i in range(len(arr)):
    #     print(arr[-1 - i])
    #     if arr[i] != arr[-1 - i]:
    #         palin_check = False
    #         break




if __name__ == '__main__':
    s = "abb"
    res = removePalindromeSub(s)
