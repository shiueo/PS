import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

trust_arr = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    trust_arr[b - 1].append(a - 1)  # a가 b를 신뢰한다 순으로 들어오니까, b를 해킹하면 a도 해킹할 수 있음.


def count(pc):
    target = deque()
    target.append(pc)
    visited = [False] * N
    visited[pc] = True
    c = 1

    while target:
        hacked = target.popleft()
        for k in trust_arr[hacked]:
            if not visited[k]:
                target.append(k)
                c += 1
                visited[k] = True
    return c


res = []
for i in range(N):
    res.append(count(i))

m_val = max(res)
for i in range(len(res)):
    if res[i] == m_val:
        print(i+1, end=' ')