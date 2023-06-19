import sys

Y, X = map(int, sys.stdin.readline().split())

L = [list(map(int, sys.stdin.readline().split())) for _ in range(Y)]
dp = [[-1] * X for _ in range(Y)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def dfs(x, y):
    if x == Y - 1 and y == X - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < Y and 0 <= next_y < X:
            if L[next_x][next_y] < L[x][y]:  # 내리막길
                dp[x][y] += dfs(next_x, next_y)

    return dp[x][y]


print(dfs(0, 0))
