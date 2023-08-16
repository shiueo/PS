import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

L = []


def DFS(start):
    if len(L) == M:
        print(*L)
        return
    for i in range(start, N + 1):
        L.append(i)
        DFS(i)
        L.pop()


DFS(1)
