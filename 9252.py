import sys

A = [""]+list(sys.stdin.readline().strip())
B = [""]+list(sys.stdin.readline().strip())

L_A, L_B = len(A), len(B)
dp = [["" for _ in range(L_A)] for _ in range(L_B)]

for i in range(1, L_B):
    for j in range(1, L_A):
        if B[i] == A[j]:
            dp[i][j] = dp[i - 1][j - 1] + B[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]), dp[-1][-1], sep="\n")

