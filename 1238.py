import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

GRAPH = [[] for _ in range(N)]
for _ in range(M):
    A, B, T = map(int, sys.stdin.readline().split())
    GRAPH[A - 1].append([B-1, T])


def dijkstra(start_point):
    q = []
    heapq.heappush(q, (0, start_point))
    distance[start_point] = 0
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for i in GRAPH[curr]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


res = []
tl = []
for i in range(N):
    distance = [1e9] * (N+1)
    res.append(dijkstra(i))
for i in range(N):
    tl.append(res[i][X-1] + res[X-1][i])
print(max(tl))
