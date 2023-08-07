import sys

N, M = map(int, sys.stdin.readline().split())

k = dict()
for i in range(N):
    site, pw = map(str, sys.stdin.readline().split())
    k[site] = pw

for i in range(M):
    print(k[sys.stdin.readline().strip()])