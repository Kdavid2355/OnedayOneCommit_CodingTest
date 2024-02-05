import sys
input=sys.stdin.readline

n, q = map(int, input().split())
l = list(map(int, input().split()))

prefix = [0]
temp = 0
for i in l:
    temp = temp + i
    prefix.append(temp)

for j in range(q):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start-1])


