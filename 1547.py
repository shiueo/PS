import sys

N = int(sys.stdin.readline())

LL = [1, 2, 3, 4]
for i in range(N):
    R, P = map(int, sys.stdin.readline().split())
    R, P = LL.index(R), LL.index(P)
    LL[R], LL[P] = LL[P], LL[R]
print(LL[0])
