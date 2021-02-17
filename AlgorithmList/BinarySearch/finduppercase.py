
input_str1 = "LucidProgramming"

def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase"

def find_uppercase_recursive(input_str,idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str)-1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str,idx+1)

print(find_uppercase_iterative(input_str1))