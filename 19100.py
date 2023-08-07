import sys

n, t = map(int, sys.stdin.readline().split())
g = list(map(int, sys.stdin.readline().split()))

if t % 2:
    print(*reversed(g))
else:
    print(*g)
