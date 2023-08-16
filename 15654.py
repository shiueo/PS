import sys
import itertools


N, M = map(int, sys.stdin.readline().split())

L = list(map(int, sys.stdin.readline().split()))
L.sort()
for i in itertools.permutations(L, M):
    print(*i)
