import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(L[0])
else:
    DP = [[0]*N for _ in range(2)]
    DP[0][0] = L[0]
    DP[1][0] = L[0]
    for i in range(1, N):
        DP[0][i] = max(DP[0][i-1]+L[i], L[i])
        DP[1][i] = max(DP[0][i-1], DP[1][i-1] + L[i])

    print(max(max(DP[0]), max(DP[1])))