import sys

N = int(sys.stdin.readline())

for j in range(2 * N - 1, 0, -2):
    s = " " * ((2 * N - 1 - j) // 2) + "*" * j
    print(s)
