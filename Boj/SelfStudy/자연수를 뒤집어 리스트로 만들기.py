def digit_reverse(n):
    list = [int(i) for i in str(n)]
    list.reverse()
    return list

n=12345
digit_reverse(n)