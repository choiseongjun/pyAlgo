import sys
import collections
def removeDuplicateLetters(s):
    stack=[]
    counter,seen,stack = collections.Counter(s),set(),[]

    print(counter)
    for char in s:
        counter[char] -=1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    print(''.join(stack))



s="bcabc"
removeDuplicateLetters(s)