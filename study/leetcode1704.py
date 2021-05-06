def halvesAreAlike( s):

    case= {'a','e','i','o','u','A','E','I','O','U'}
    cnt=0
    cnt1=0
    check=False
    for i in range(len(s)//2):
        if s[i] in case:
            cnt+=1
        for j in s[-1-i]:
            if j in case:
                cnt1+=1

        if cnt!=cnt1:
            check = False
        else:
            check = True

    return check

if __name__ == '__main__':
    #s = "textbook"
    s = "AbCdEfGh"
    halvesAreAlike(s)
