import sys
class stack:
    def __init__(self):
        self.items=[]
    def push(self,n):
        self.items.append(n)
    def pop(self):
        if len(self.items)==0:
            return -1
        return self.items.pop()
    def isEmpty(self):##비어있으면 1 아니면 0
        if len(self.items)==0:
            print(1)
        else:
            print(0)
    def peek(self):
        if len(self.items) == 0:
            return -1
        return self.items[-1]
    def size(self):
        return len(self.items)

stk=stack()
a = sys.stdin.readline##/시간 초과 방지
a=int(a())
for i in range(a):
    text= sys.stdin.readline().split()#시간 초과방지
    if text[0]=='push':
        stk.push(text[1])
    elif text[0]=='pop':
        print(stk.pop())
    elif text[0]=='size':
        print(stk.size())
    elif text[0]=='empty':
        stk.isEmpty()
    elif text[0]=='top':
        print(stk.peek())