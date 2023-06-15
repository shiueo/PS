import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n)]

if n >= 3:
    dp[0]=1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[-1] % 10007)
else:
    if n == 2:
        print(2)

    else:
        print(1)
