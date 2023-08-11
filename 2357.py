import math
import sys

sys.setrecursionlimit(10 ** 8)
N, M = map(int, sys.stdin.readline().split())

L = [int(sys.stdin.readline()) for _ in range(N)]

height = math.ceil(math.log2(N)) + 1
node_N = 1 << height
segment = [0 for _ in range(node_N)]


def SegmentTree(index, start, end):
    if start == end:
        segment[index] = (L[start], L[end])
        return segment[index]

    mid = (start + end) // 2

    l = SegmentTree(index * 2, start, mid)
    r = SegmentTree(index * 2 + 1, mid + 1, end)
    segment[index] = (min(l[0], r[0]), max(l[1], r[1]))

    return segment[index]


def get(index, start, end, range_1, range_2):
    if range_2 < start or range_1 > end:
        return 10 ** 9 + 1, 0
    if range_1 <= start and range_2 >= end:
        return segment[index]

    mid = (start + end) // 2
    l = get(index * 2, start, mid, range_1, range_2)
    r = get(index * 2 + 1, mid + 1, end, range_1, range_2)

    return min(l[0], r[0]), max(l[1], r[1])


SegmentTree(1, 0, len(L) - 1)

for i in range(M):
    r1, r2 = map(int, sys.stdin.readline().split())
    r1 -= 1
    r2 -= 1
    g1, g2 = get(1, 0, len(L) - 1, r1, r2)
    print(g1, g2)
