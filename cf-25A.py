import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
odd, even = 0, 0
for i in range(n):
    if L[i] % 2 == 0:
        even += 1
        L[i] = 0
    else:
        odd += 1
        L[i] = 1

if odd > even:
    print(L.index(0)+1)
else:
    print(L.index(1)+1)
