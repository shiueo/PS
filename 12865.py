import sys

N, K = map(int, sys.stdin.readline().split())

L = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, 1 + N):
    for j in range(1, 1 + K):
        w, v = L[i]
        if j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
