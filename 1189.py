import sys

R, C, K = map(int, sys.stdin.readline().split())

MATRIX = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

RES = 0


def DFS(pos_x, pos_y, curr_distance):
    global RES
    if curr_distance == K and pos_x == 0 and pos_y == C - 1:
        RES += 1
    else:
        for i in range(4):
            next_x, next_y = pos_x + dx[i], pos_y + dy[i]
            if 0 <= next_x < R and 0 <= next_y < C and MATRIX[next_x][next_y] == ".":
                MATRIX[next_x][next_y] = 'T'
                DFS(next_x, next_y, curr_distance + 1)
                MATRIX[next_x][next_y] = "."


MATRIX[R-1][0] = 'T'
DFS(R - 1, 0, 1)
print(RES)
