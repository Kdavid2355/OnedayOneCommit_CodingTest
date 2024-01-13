import sys
input=sys.stdin.readline

n = int(input())
sentences = []
for i in range(n):
    stn = input()
    sentences += stn.split("\n")

sentences = [i for i in sentences if i != '']

for words in sentences:
    word = words.split(' ')
    for s in word:
        print(s[::-1], end=' ')
    print()