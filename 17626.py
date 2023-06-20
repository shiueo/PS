import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N + 1)]

if N > 4:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 1
    for i in range(5, N + 1):
        min_value = 5
        j = 1
        while (j**2) <= i:
            min_value = min(min_value, dp[i - (j**2)])
            j += 1
        dp[i] = min_value + 1

    print(dp[N])
else:
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(3)
    elif N == 4:
        print(1)
