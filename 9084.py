import sys

N = int(sys.stdin.readline())

for i in range(N):
    import sys

    V = int(sys.stdin.readline())

    Coins = list(map(int, sys.stdin.readline().split()))
    K = int(sys.stdin.readline())

    dp = [0] * (K + 1)
    dp[0] = 1
    for coin in Coins:
        for j in range(1, K + 1):
            if j >= coin:
                dp[j] += dp[j - coin]
    print(dp[K])
