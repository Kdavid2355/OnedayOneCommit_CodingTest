import sys
input=sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack = input().rstrip('\n')
    l = []
    for i in stack:
        if i == "(":
            l.append(i)
        elif i == ")":
            try:
                l.pop()
            except:
                l.append(i)
                break

    if len(l) == 0:
        print("YES")
    else:
        print("NO")




