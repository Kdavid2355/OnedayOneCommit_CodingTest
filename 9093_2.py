import sys
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    stn = input().rstrip()
    words = stn.split(' ')
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])

    answer = " ".join(reversed_words)
    print(answer)