
#참조 하였음
def makeGood(s):

    stack = []

    for char in s:
        if stack and stack[-1].swapcase()==char:
            stack.pop(-1)
        else:
            stack.append(char)
    res=""
    while stack:
        res+=stack.pop(-1)
    return res[::-1]


if __name__ == '__main__':
    str="abBAcC"
    makeGood(str)