import heapq
import sys

N, E = map(int, sys.stdin.readline().split())

GRAPH = [[] for _ in range(N)]
for i in range(E):
    A, B, X = map(int, sys.stdin.readline().split())
    GRAPH[A - 1].append((B-1, X))
    GRAPH[B - 1].append((A-1, X))
U, V = map(int, sys.stdin.readline().split())


def dijkstra(start_point):
    visited = [1e9] * N
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


to_end = dijkstra(0)
u_d = dijkstra(U - 1)
v_d = dijkstra(V - 1)

final_dist = min(to_end[U - 1] + u_d[V - 1] + v_d[N - 1], to_end[V - 1] + v_d[U - 1] + u_d[N - 1])

if final_dist >= 1e9:
    print(-1)
else:
    print(final_dist)
