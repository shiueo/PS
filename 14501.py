import sys

N = int(sys.stdin.readline())

L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    if i + L[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(L[i][1] + dp[i + L[i][0]], dp[i + 1])

print(dp[0])
