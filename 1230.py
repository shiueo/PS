import sys

O = sys.stdin.readline().strip()
N = sys.stdin.readline().strip()
L1 = len(O)
L2 = len(N)
INF = 10000
dp = [[INF] * L2 for _ in range(L1)]
for i in range(L2):
    if O[0] == N[i]:
        if i == 0 or i == L2 - 1:
            dp[0][i] = 1
        else:
            dp[0][i] = 2

for i in range(1, L1):
    check = INF
    for j in range(i):
        check = min(check, dp[i - 1][j])
    for j in range(i, L2):
        if O[i] == N[j]:
            if O[i - 1] == N[j - 1] and dp[i - 1][j - 1] == check:
                dp[i][j] = check
            else:
                dp[i][j] = min(INF, check + 1)
        check = min(check, dp[i - 1][j])

if O[-1] == N[-1] and dp[-1][-1] != INF:
    dp[-1][-1] -= 1
res = INF
for i in range(L2):
    res = min(res, dp[-1][i])
if res == INF:
    print(-1)
else:
    print(res)
