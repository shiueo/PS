import sys

N, M = map(int, sys.stdin.readline().split())

MATRIX_A = []
for _ in range(N):
    MATRIX_A.append(list(map(int, list(sys.stdin.readline().strip()))))

MATRIX_B = []
for _ in range(N):
    MATRIX_B.append(list(map(int, list(sys.stdin.readline().strip()))))

if (N < 3 or M <3) and MATRIX_A != MATRIX_B:
    print("-1")
    sys.exit()
else:
    count = 0
    for x in range(N-2):
        for y in range(M-2):
            if MATRIX_A[x][y] != MATRIX_B[x][y]:
                count += 1
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if MATRIX_A[i][j] == 0:
                            MATRIX_A[i][j] = 1
                        else:
                            MATRIX_A[i][j] = 0

if MATRIX_A != MATRIX_B:
    print(-1)
else:
    print(count)