def change_binary(n : int) -> int:
    result, idx = 0,0
    while (n >=1):
        remainder =n % 2
        n = n // 2
        result += (10**idx)* remainder
        idx +=1
    return result
n=13
a=change_binary(n)
print(a)