import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

GRAPH = [[] for _ in range(N+1)]

for i in range(N - 1):
    a, b, l = map(int, sys.stdin.readline().split())
    GRAPH[a].append((b, l))
    GRAPH[b].append((a, l))


def BFS(start_node, end_node):
    Q = deque()
    Q.append((start_node, 0))
    visited = [False] * (N + 1)
    visited[start_node] = True
    while Q:
        next_node, length = Q.popleft()
        if next_node == end_node:
            return length

        for n_node, l_length in GRAPH[next_node]:
            if not visited[n_node]:
                visited[n_node] = True
                Q.append((n_node, l_length+length))


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(BFS(a, b))
