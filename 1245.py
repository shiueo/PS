import sys
import time
from collections import deque

N, M = map(int, sys.stdin.readline().split())

GRID = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

visited = []

global isM


def bfs(x, y):
    global isM
    to_visit = deque([(x, y)])
    visited.append([x, y])

    while to_visit:
        X, Y = to_visit.popleft()
        for d in range(8):
            near_x, near_y = X + dx[d], Y + dy[d]
            if 0 <= near_x < N and 0 <= near_y < M:
                if GRID[near_x][near_y] > GRID[X][Y]:
                    isM = False
                if GRID[near_x][near_y] == GRID[X][Y] and not [near_x, near_y] in visited:
                    to_visit.append((near_x, near_y))
                    bfs(near_x, near_y)


cnt = 0
for i in range(N):
    for j in range(M):
        if GRID[i][j] != 0 and not [i, j] in visited:
            isM = True
            bfs(i, j)
            if isM:
                cnt += 1
print(cnt)
