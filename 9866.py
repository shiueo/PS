import heapq
import sys

N, M, K, Q = map(int, sys.stdin.readline().split())

GRAPH, inv_GRAPH = [[] for _ in range(N + 1)], [[] for _ in range(N + 1)]
for _ in range(M):
    u_i, v_i, d_i = map(int, sys.stdin.readline().split())
    GRAPH[u_i].append((v_i, d_i))
    inv_GRAPH[v_i].append((u_i, d_i))

HUBS = []
for _ in range(K):
    HUBS.append(int(sys.stdin.readline()))

visited = [[[20001] * (N + 1) for _ in range(2)] for _ in range(K)]


def dijkstra(start_point, matrix, num, t):
    heap = []
    heapq.heappush(heap, (0, start_point))
    visited[num][t][start_point] = 0
    while heap:
        dist, point = heapq.heappop(heap)
        if dist > visited[num][t][point]:
            continue

        for i, j in matrix[point]:
            cost = dist + j
            if cost < visited[num][t][i]:
                visited[num][t][i] = cost
                heapq.heappush(heap, (cost, i))


for i in range(K):
    dijkstra(HUBS[i], GRAPH, i, 0)
    dijkstra(HUBS[i], inv_GRAPH, i, 1)

c = 0
cost = 0
A = []
for client in range(Q):
    s, a = map(int, sys.stdin.readline().split())

    minimum_val = 20001
    for i in range(K):
        minimum_val = min(minimum_val, visited[i][1][s]+visited[i][0][a])
    if minimum_val != 20001:
        cost += minimum_val
        c+=1

print(c)
print(cost)
