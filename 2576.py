import sys

L = []

for i in range(7):
    k = int(sys.stdin.readline())
    if k % 2 == 1:
        L.append(k)

if L:
    print(sum(L))
    print(min(L))
else:
    print("-1")
