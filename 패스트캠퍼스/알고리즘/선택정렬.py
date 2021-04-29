def selection_sort(data):
    for stand in range(len(data)-1):
        print(stand)
        lowest = stand
        for index in range(stand+1,len(data)):
            if data[lowest]>data[index]:
                lowest = index
        data[lowest],data[index] = data[index],data[lowest]
    return data

if __name__ == '__main__':
    res = selection_sort([3,4,1,2])
    print(res)