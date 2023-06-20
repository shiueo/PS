import sys

L = int(sys.stdin.readline())

C = list(map(int, sys.stdin.readline().split()))

ASCENT, DESCENT = [1 for _ in range(L)], [1 for _ in range(L)]

for i in range(L):
    for j in range(i):
        if C[i] > C[j]:
            ASCENT[i] = max(ASCENT[i], ASCENT[j] + 1)

for i in range(L - 1, -1, -1):
    for j in range(L - 1, i, -1):
        if C[i] > C[j]:
            DESCENT[i] = max(DESCENT[i], DESCENT[j] + 1)

res = [0 for _ in range(L)]
for i in range(L):
    res[i] = ASCENT[i] + DESCENT[i] - 1
print(max(res))
