import sys
def removeDuplicateLetters(s):
    stack=[]
    for i in range(len(s)):
        for j in range(len(s)):
            if i==j:
                continue
            print(s[j])






s="bcabc"
removeDuplicateLetters(s)