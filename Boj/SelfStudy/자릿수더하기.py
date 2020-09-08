def sum_digit(number):
    sum=0
    for i in str(number):
        sum+=int(i)
    print(sum)

number=123
sum_digit(number)