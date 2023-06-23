import sys

N, M = map(int, sys.stdin.readline().split())

L = [list(sys.stdin.readline().strip()) for _ in range(N)]
U = [[0] * (M + 1) for _ in range(N + 1)]

max_v = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if L[i - 1][j - 1] == '1':
            U[i][j] = min(int(U[i - 1][j]), int(U[i][j - 1]), int(U[i - 1][j - 1])) + 1
    max_v = max(max_v, max(U[i]))
print(max_v ** 2)
