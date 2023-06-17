import sys

A, B = map(int, sys.stdin.readline().split())

MATRIX = [list(map(int, sys.stdin.readline().split())) for _ in range(A)]
TO_GET = [list(map(int, sys.stdin.readline().split())) for _ in range(B)]

SUM_MATRIX = [[0 for i in range(A+1)] for j in range(A+1)]
for i in range(1, A+1):
    for j in range(1, A+1):
        SUM_MATRIX[i][j] = SUM_MATRIX[i][j-1] + SUM_MATRIX[i-1][j] - SUM_MATRIX[i-1][j-1] + MATRIX[i-1][j-1]

for i in range(B):
    print(SUM_MATRIX[TO_GET[i][2]][TO_GET[i][3]] - SUM_MATRIX[TO_GET[i][2]][TO_GET[i][1]-1] - SUM_MATRIX[TO_GET[i][0]-1][TO_GET[i][3]] + SUM_MATRIX[TO_GET[i][0]-1][TO_GET[i][1]-1])