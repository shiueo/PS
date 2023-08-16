import sys
import itertools

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))
K = dict()
for i in L:
    K[i] = 0

table = [False for _ in range(1000001)]

for i in L:
    table[i] = True

for i in sorted(L):
    for j in range(2*i, 1000001, i):
        if table[j]:
            K[i] += 1
            K[j] -= 1

print(*K.values())