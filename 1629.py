import sys

A, B, C = map(int, sys.stdin.readline().split())


def s(a, b):
    if b == 1:
        return a % C

    d = s(a, b // 2)
    if b % 2 == 0:
        return d * d % C
    else:
        return d * d * A % C


print(s(A, B))
