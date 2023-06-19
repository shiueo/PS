import sys

N, K = map(int, sys.stdin.readline().split())

Coins = [int(sys.stdin.readline()) for _ in range(N)]

dp = [10001] * (K + 1)
dp[0] = 0
for coin in Coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
