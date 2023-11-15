import math
import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
U = []
for i in range(1, len(L)):
    U.append(L[i] - L[i - 1])

v = U[0]
for i in U:
    v = math.gcd(v, i)
print(v)
