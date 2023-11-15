import sys
import time

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
R = [0] * N
for i in range(1, N+1):
    k = L[i-1]
    cnt = 0
    for j in range(N):
        if cnt == k and R[j] == 0:
            R[j] = i
            break
        elif R[j] == 0:
            cnt += 1
print(*R)
