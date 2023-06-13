import sys

N, M = map(int, sys.stdin.readline().split())

L = []
for i in range(N):
    L.append(list(sys.stdin.readline().strip()))

res = []
for i in range(N):
    for j in range(M):
        tmp = L[i][j]
        for k in range(j, M):
            if L[i][k] == tmp and i + k - j < N and k < M:
                if L[i + k - j][j] == tmp and L[i + k - j][k] == tmp:
                    res.append((k - j + 1) ** 2)

print(max(res))
