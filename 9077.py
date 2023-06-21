import sys

TEST_CASE_NUM = int(sys.stdin.readline())
field = [[0] * 10001 for _ in range(10001)]
for i in range(TEST_CASE_NUM):
    MINE_NUM = int(sys.stdin.readline())
    LOC = [list(map(int, sys.stdin.readline().split())) for _ in range(MINE_NUM)]

    for loc in LOC:
        start_x, end_x, start_y, end_y = 0, 0, 0, 0
        if loc[0] + 10 <= 10000:
            start_x = loc[0]
            end_x = loc[0] + 10
        else:
            start_x = loc[0]
            end_x = 10000

        if loc[1] + 10 <= 10000:
            start_y = loc[1]
            end_y = loc[1] + 10
        else:
            start_y = loc[1]
            end_y = 10000

        for xx in range(start_x, end_x + 1):
            for yy in range(start_y, end_y + 1):
                field[xx][yy] += 1

    max_v = 0
    for iii in field:
        max_v = max(max_v, max(iii))
    print(max_v)

    for xxx in range(10001):
        for yyy in range(10001):
            field[xxx][yyy] = 0
