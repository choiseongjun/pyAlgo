from collections import Counter
#다시 공부하기
def removeDuplicateLetters(s):
    stack=[]
    counter = Counter()

    for char in s:
        if char in stack:
            continue

        # while stack and char < stack[-1]and counter[stack[-1]]>0:
        #     stack.pop()
        stack.append(char)
    return "".join(stack)


if __name__ == '__main__':
    str = "bcabc"
    removeDuplicateLetters(str)