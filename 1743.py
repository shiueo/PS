import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())

GRID = [['.' for _ in range(M)] for _ in range(N)]

for i in range(K):
    r, c = map(int, sys.stdin.readline().split())
    GRID[r - 1][c - 1] = '#'

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(y, x):
    cnt = 0
    to_visit = deque([(y, x)])
    visited[y][x] = True
    while to_visit:
        pos_y, pos_x = to_visit.popleft()
        cnt += 1
        for d in range(4):
            next_y, next_x = pos_y + dy[d], pos_x + dx[d]
            if 0 <= next_y < N and 0 <= next_x < M and not visited[next_y][next_x] and GRID[next_y][next_x] == "#":
                to_visit.append((next_y, next_x))
                visited[next_y][next_x] = True

    return cnt


res = 0
for y in range(N):
    for x in range(M):
        if GRID[y][x] == "#":
            res = max(res, bfs(y, x))

print(res)