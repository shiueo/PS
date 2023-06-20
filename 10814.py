import sys

N = int(sys.stdin.readline())


L = [sys.stdin.readline().split() for _ in range(N)]
L.sort(key=lambda x: int(x[0]))

for i in L:
    print(i[0], i[1])
