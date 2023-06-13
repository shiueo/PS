import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

D = deque()

for i in range(1, 1 + N):
    D.append(i)

RES = []
while D:
    for _ in range(K - 1):
        D.append(D.popleft())
    RES.append(str(D.popleft()))

print(f"<{', '.join(RES)}>")
