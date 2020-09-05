n=int(input())
check=False
for i in range(1,n):
    dsum=0
    for j in str(i):
        dsum+=int(j)
    if i+dsum==n:
        check=True
        break

if check:
    print(i)
else:
    print(0)

    #num_list=list(map(int,str(i)))
    # print(i)
    # answer=i+sum(num_list)
    #
    # if answer==n:
    #     print(i)
    #     break
    # if i==n:
    #     print(0)



# while n>0:
#     res=n%10
#     n//=10
#     sum+=res
#
# print(sum)