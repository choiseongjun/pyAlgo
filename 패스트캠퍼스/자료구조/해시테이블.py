

def hash_func(key):
    return key%5

# data1='Andy'
# data2='Dave'
# data3='Trump'
#
# hash_table = list([0 for i in range(10)])
# #ord():문자의 아스키 코드 리턴
# def storage_data(data,value):
#     key=ord(data[0])
#     hash_address=hash_func(key)
#     hash_table[hash_address] = value
#
# storage_data('Andy','01055553333')
# storage_data('Dave','01044443333')
# storage_data('Trump','01022223333')
#
# def get_data(data):
#     key = ord(data[0])
#     hash_address=hash_func(key)
#     return hash_table[hash_address]

# print(get_data('Andy'))

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data,value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave','01020300200')
save_data('Andy','01033232200')
# print(read_data('Dave'))
print(hash_table)

#칼리션 해결
def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(get_key(data))
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1]=value
                return
        hash_table[hash_address].append([index_key,value])
    else:
        hash_table[hash_address] = list([index_key,value])
        

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]