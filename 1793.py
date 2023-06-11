import sys

dp = [0 for i in range(251)]

while 1:
    try:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        n = int(sys.stdin.readline())
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + 2 * dp[i - 2]
        print(dp[n])
    except:
        break
