import sys
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.stack.pop())

    def top(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.stack[-1])

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        print(len(self.stack))
        return len(self.stack)



lst = Stack()
n = sys.stdin.readline()
for i in range(int(n)):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        lst.push(order[1])
    elif order[0] == "top":
        lst.top()
    elif order[0] == "size":
        lst.size()
    elif order[0] == "empty":
        if lst.size() > 0:
            print(0)
        else:
            print(1)
    elif order[0] == "pop":
        lst.pop()
