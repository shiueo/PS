import sys

points_num, lines_num, start_pos = map(int, sys.stdin.readline().split())

nodes = [[]] * (1 + points_num)
visited = [0] * (1 + points_num)
for i in range(lines_num):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

for i in range(len(nodes)):
    nodes[i].sort()

dfs = []
bfs = []


def DFS(v):
    visited[v] = 1
    dfs.append(v)
    for i in nodes[v]:
        if visited[i] == 0:
            DFS(i)


DFS(start_pos)
visited = [0] * (points_num+1)


def BFS(v):
    visited[v] = 1
    bfs.append(v)
    queue = [v]
    while queue:
        for i in nodes[queue.pop(0)]:
            if visited[i] == 0:
                visited[i] = 1
                bfs.append(i)
                queue.append(i)


BFS(start_pos)
print(' '.join(map(str, dfs)))
print(' '.join(map(str, bfs)))
