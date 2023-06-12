import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

K = [1]
for i in range(1, N):
    u = []
    for j in range(i):
        if L[i] > L[j]:
            u.append(K[j] + 1)

    if not u:
        K.append(1)
    else:
        K.append(max(u))

print(max(K))
