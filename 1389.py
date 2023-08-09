import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    matrix[A - 1].append(B - 1)
    matrix[B - 1].append(A - 1)

def BFS(start):
    visited = [start]
    q = deque()
    q.append(start)

    bacon_number = [0] * N
    while q:
        next = q.popleft()
        for friend in matrix[next]:
            if friend not in visited:
                bacon_number[friend] = bacon_number[next] + 1
                visited.append(friend)
                q.append(friend)
    return sum(bacon_number)


res = []
for i in range(N):
    res.append(BFS(i))
print(res.index(min(res)) + 1)
