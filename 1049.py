import sys

N, M = map(int, sys.stdin.readline().split())

SECHT = []
EIN = []
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    SECHT.append(A)
    EIN.append(B)

SECHT.sort()
EIN.sort()

if SECHT[0] <= EIN[0] * 6:
    RES = SECHT[0] * (N // 6) + EIN[0] * (N % 6)
    if SECHT[0] < EIN[0] * (N % 6):
        RES = SECHT[0] * (N // 6 + 1)
else:
    RES = EIN[0] * N

print(RES)
