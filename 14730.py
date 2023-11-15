import sys

N = int(sys.stdin.readline())

s = 0
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())

    s += r * c

print(s)
