import sys

N = int(sys.stdin.readline())

IN = [int(sys.stdin.readline()) for _ in range(N)]
U = max(IN)
if U > 3:
    dp = [0 for _ in range(U)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7
    for j in range(4, U):
        dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009
else:
    dp = [0 for _ in range(4)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7

for i in IN:
    print(dp[i - 1])
