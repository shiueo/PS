import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

dp = [[0]*21 for _ in range(N)]

dp[0][L[0]] += 1
for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j + L[i] < 21:
                dp[i][j+L[i]] += dp[i-1][j]
            if j - L[i] > -1:
                dp[i][j-L[i]] += dp[i-1][j]
print(dp[N-2][L[N-1]])
