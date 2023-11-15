import sys

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x


for i in range(m):
    sign, a, b = map(int, sys.stdin.readline().split())
    if sign == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('yes')
        else:
            print('no')
