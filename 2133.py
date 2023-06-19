"""
홀수는 다 못 채우고

2일 때는 3
4일 때는 2일 때 붙인거를 조합이므로
"""
import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3

for i in range(4, N + 1):
    dp[i] = dp[i - 2] * 3
    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2

print(dp[N])
