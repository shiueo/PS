import sys

K, X = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

LL = [0]
c = 0
for i in L:
    c += i
    LL.append(c)
for i in range(X):
    O, P = map(int, sys.stdin.readline().split())
    if O == P:
        print(L[O - 1])
    else:
        print(LL[P] - LL[O-1])
