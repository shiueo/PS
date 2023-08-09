import sys

N, r, c = map(int, sys.stdin.readline().split())


def Z(N_1, r_1, c_1):
    if N_1 == 0:
        return 0
    else:
        return 2 * (r_1 % 2) + (c_1 % 2) + 4 * Z(N_1 - 1, r_1 // 2, c_1 // 2)


print(Z(N, r, c))
