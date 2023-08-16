import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

c = 0
min_val, max_val = L[0], L[0]
for i in range(1, N):
    tmp_max_val, tmp_min_val = max_val, min_val
    if L[i] > max_val:
        max_val = L[i]
    if L[i] < min_val:
        min_val = L[i]
    if tmp_max_val != max_val or tmp_min_val != min_val:
        c += 1
print(c)
