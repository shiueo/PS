import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

K = [1 for _ in range(N)]
for i in range(N, -1, -1):
    for j in range(N-1, i, -1):
        if L[i] > L[j]:
            K[i] = max(K[i], K[j]+1)

print(max(K))