"""
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
"""
import sys

N = int(sys.stdin.readline())

dp = []
for i in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(0, len(dp[i])):
        if j == 0:
            dp[i][0] += dp[i - 1][0]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))
