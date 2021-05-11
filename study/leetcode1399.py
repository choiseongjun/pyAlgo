def largestAltitude(gain):

    li=[0]
    for i in range(len(gain)):
        li.append(li[i]+gain[i])
    return max(li)


if __name__ == '__main__':
    n=[-5,1,5,0, -7]
    res = largestAltitude(n)
    print(res)