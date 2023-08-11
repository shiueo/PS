import sys
from itertools import permutations

N, F = map(int, sys.stdin.readline().split())


def get_last_num(arr):
    if len(arr) == 1:
        return arr[0]
    next_arr = []
    for i in range(len(arr) - 1):
        next_arr.append(arr[i] + arr[i + 1])
    return get_last_num(next_arr)


for i in permutations(range(1, N + 1)):
    if get_last_num(i) == F:
        print(*i)
        break
