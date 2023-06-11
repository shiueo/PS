import sys

N, K = map(int, sys.stdin.readline().split())

MOD_V = 1000000000

dp = [[0] * (N + 1) for i in range(K + 1)]
dp[0][0] = 1

for i in range(1, K + 1):
    for j in range(N + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD_V

print(dp[K][N])
