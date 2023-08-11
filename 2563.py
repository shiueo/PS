import sys

N = int(sys.stdin.readline())
poses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

board = [[0] * 100 for _ in range(100)]

for i in poses:
    for x in range(i[0], i[0] + 10):
        for y in range(i[1], i[1] + 10):
            board[x][y] = 1

s = 0
for i in board:
    s += sum(i)
print(s)
