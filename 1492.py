import sys

N, K = map(int, sys.stdin.readline().split())

MOD = 1000000007
modulo = [[0 for _ in range(52)] for _ in range(52)]
dp = [0 for _ in range(51)]


for i in range(52):
    modulo[i][0], modulo[i][i] = 1, 1
    for j in range(i):
        modulo[i][j] = modulo[i - 1][j] + modulo[i - 1][j - 1] % MOD

dp[0] = N
for i in range(1, K + 1):
    tmp = pow(N + 1, i + 1, MOD) - 1
    for j in range(i):
        tmp -= modulo[i + 1][j] * dp[j] % MOD
        if tmp < 0:
            tmp = (tmp + MOD) % MOD
        else:
            tmp %= MOD
    tmp = tmp * pow(modulo[i + 1][i], MOD - 2, MOD) % MOD
    dp[i] = tmp

print(dp[K])
