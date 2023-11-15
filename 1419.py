import sys

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())
k = int(sys.stdin.readline())

if k % 2:
    t = (k + 1) // 2
    L = (l + k - 1) // k
    R = r // k
    if t > R:
        print(0)
    else:
        print(R - max(L, t) + 1)
else:
    t = k + 1
    L = (l + k // 2 - 1) // (k // 2)
    R = r // (k // 2)
    bias = int(k == 4) * int(L <= 6 <= R)
    if t > R:
        print(0)
    else:
        print(R - max(L, t) + 1 - bias)
