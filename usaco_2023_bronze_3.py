import sys

N, K = map(int, sys.stdin.readline().split())

schedule = list(map(int, sys.stdin.readline().split()))

res = 1 + K
for i in range(1, N):
    gap = schedule[i] - schedule[i - 1]
    if gap <= K:
        res += gap
    else:
        res += 1 + K

print(res)
