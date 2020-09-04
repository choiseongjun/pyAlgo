import sys
class ArrayQueue:
    def __init__(self):
        self.queue=[]

    def add(self,n):
        self.queue.append(n)
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(0)
    def peek(self):
        if len(self.queue)==0:
            return -1
        return self.queue[-1]
    def isEmpty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        if len(self.queue)==0:
            return -1
        
        return self.queue[0]
    def back(self):
        if len(self.queue)==0:
            return -1

        return self.queue[-1]
    def size(self):
        return len(self.queue)


que=ArrayQueue()
a = sys.stdin.readline#시간 초과 방지
a=int(a())
for i in range(a):
    text = sys.stdin.readline().split()  # 시간 초과방지
    if text[0]=='push':
        que.add(text[1])
    elif text[0]=='pop':
        print(que.pop())
    elif text[0]=='size':
        print(que.size())
    elif text[0]=='empty':
        que.isEmpty()
    elif text[0]=='front':
        print(que.front())
    elif text[0]=='back':
        print(que.back())