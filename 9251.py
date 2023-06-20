import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

L_A, L_B = len(A), len(B)
dp = [[0 for _ in range(L_A + 1)] for _ in range(L_B + 1)]

for i in range(1, L_B + 1):
    for j in range(1, L_A + 1):
        if B[i - 1] == A[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
