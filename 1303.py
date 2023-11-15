import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

GRID = [list(sys.stdin.readline().strip()) for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(y, x, C):
    to_visit = deque([(y, x)])
    GRID[y][x] = "K"

    cnt = 0

    while to_visit:
        Y, X = to_visit.popleft()
        cnt += 1
        for d in range(4):
            next_Y, next_X = Y + dy[d], X + dx[d]
            if 0 <= next_Y < M and 0 <= next_X < N:
                if not GRID[next_Y][next_X] == "K" and GRID[next_Y][next_X] == C:
                    GRID[next_Y][next_X] = True
                    to_visit.append((next_Y, next_X))
    return cnt**2


W = 0
for y in range(M):
    for x in range(N):
        if GRID[y][x] == "W":
            W += bfs(y, x, "W")

B = 0
for y in range(M):
    for x in range(N):
        if GRID[y][x] == "B":
            B += bfs(y, x, "B")

print(W, B)
