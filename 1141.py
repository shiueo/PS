import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]
prefix = [False] * N

words.sort(key=len)
res = 0
for i in range(N):
    for j in range(i + 1, N):
        if words[i] == words[j][0:len(words[i])]:
            prefix[i] = True
            break
    if not prefix[i]:
        res += 1
print(res)
