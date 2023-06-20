import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if L[i] > L[j]:
            dp[i] = max(dp[i], dp[j] + 1)

M = max(dp)
print(M)

res = []
for i in range(N - 1, -1, -1):
    if dp[i] == M:
        res.append(str(L[i]))
        M -= 1

res.reverse()
print(" ".join(res))
