import sys

N, K = map(int, sys.stdin.readline().split())

COINS = []
for i in range(N):
    COINS.append(int(sys.stdin.readline()))

c = 0
for i in COINS[::-1]:
    if i > K:
        continue
    else:
        c += K // i
        K %= i

print(c)
