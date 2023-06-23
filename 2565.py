import sys

N = int(sys.stdin.readline())
U = []
for i in range(N):
    U.append(list(map(int, sys.stdin.readline().split())))

U.sort(key=lambda x: x[0])
L = []
for i in U:
    L.append(i[1])
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if L[i] > L[j]:
            dp[i] = max(dp[i], dp[j] + 1)

M = max(dp)
print(N-M)
