import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())

visited = [[False] * (B + 1) for _ in range(1 + A)]
visited[0][0] = True

Q = deque()
Q.append((0, 0))

answers = []


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        Q.append((x, y))


while Q:
    _a, _b = Q.popleft()
    _c = C - _a - _b
    if _a == 0:
        answers.append(_c)

    water = min(_a, B - _b)
    pour(_a - water, _b + water)
    water = min(_a, C - _c)
    pour(_a - water, _b)
    water = min(_b, C - _c)
    pour(_a, _b - water)
    water = min(_b, A - _a)
    pour(_a + water, _b - water)
    water = min(_c, A - _a)
    pour(_a + water, _b)
    water = min(_c, B - _b)
    pour(_a, _b + water)

answers.sort()
print(" ".join(list(map(str, answers))))
