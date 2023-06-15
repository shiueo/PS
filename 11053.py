import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if L[i] > L[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
