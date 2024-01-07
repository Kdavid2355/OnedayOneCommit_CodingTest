import sys

lst = []
n = sys.stdin.readline()
for i in range(int(n)):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        lst.append(int(order[1]))
    elif order[0] == "top":
        if len(lst) > 0:
            print(lst[-1])
        else:
            print(-1)
    elif order[0] == "size":
        print(len(lst))
    elif order[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "pop":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())




