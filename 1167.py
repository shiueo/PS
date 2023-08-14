import sys

V = int(sys.stdin.readline())

GRAPH = [[] for _ in range(V + 1)]

for _ in range(V):
    node = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(node) - 2, 2):
        GRAPH[node[0]].append([node[i], node[i + 1]])

visited = [-1] * (V + 1)
visited[1] = 0


def dfs(x, y):
    for a, b in GRAPH[x]:
        if -1 == visited[a]:
            visited[a] = b + y
            dfs(a, b + y)


dfs(1, 0)
start = visited.index(max(visited))
visited = [-1]*(V+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))