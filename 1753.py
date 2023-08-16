import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

GRAPH = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    GRAPH[u - 1].append((v - 1, w))


def dijkstra(start_point):
    visited = [1e9] * V
    heap = []
    heapq.heappush(heap, (0, start_point))
    visited[start_point] = 0
    while heap:
        dist, point = heapq.heappop(heap)
        if dist > visited[point]:
            continue

        for i, j in GRAPH[point]:
            cost = dist + j
            if cost < visited[i]:
                visited[i] = cost
                heapq.heappush(heap, (cost, i))
    return visited


viz = dijkstra(K - 1)

for i in viz:
    if i == 1e9:
        print("INF")
    else:
        print(i)