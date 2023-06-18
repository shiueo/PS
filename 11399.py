"""
1
1 2
1 2 3
1 2 3 3
1 2 3 3 4
"""
import sys

K = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
N.sort()
dp = [0 for _ in range(K + 1)]
for i in range(1, K + 1):
    dp[i] = dp[i - 1] + N[i-1]
print(sum(dp))