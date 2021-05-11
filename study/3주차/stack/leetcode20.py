stack = []
table = {
    '}':'{',
    ')':'(',
    ']':'[',
}


text = "()[]{}"

check = False
for s in text:
    if s not in table:
        stack.append(s)
        print(s)
    elif not stack or table[s]!=stack.pop():
        check = False

print(len(stack))