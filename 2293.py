import sys

N, K = map(int, sys.stdin.readline().split())

v = []
for i in range(N):
    v.append(int(sys.stdin.readline()))

dp = [0 for _ in range(K+1)]
dp[0] = 1
for i in v:
    for j in range(1, K + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[-1])
