import sys

n, k, l, c, d, p, nl, np = map(int, sys.stdin.readline().split())

a = k*l
b = c*d
print(min(p//np, a//nl, b) // n)