import sys

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]
for i in range(N):
    M, N, K = map(int, sys.stdin.readline().split())

    BAECHOO_BAT = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        BAECHOO_BAT[Y][X] = 1

    def dfs(x, y):
        for k in range(4):
            next_x = x + move_x[k]
            next_y = y + move_y[k]

            if 0 <= next_x < M and 0 <= next_y < N:
                if BAECHOO_BAT[next_y][next_x] == 1:
                    BAECHOO_BAT[next_y][next_x] = 0
                    dfs(next_x, next_y)

    count = 0
    for j in range(M):
        for k in range(N):
            if BAECHOO_BAT[k][j] == 1:
                count += 1
                dfs(j, k)
    print(count)
