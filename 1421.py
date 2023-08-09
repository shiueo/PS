import sys

N, C, W = map(int, sys.stdin.readline().split())
LOG = [int(sys.stdin.readline()) for _ in range(N)]

max_m = 0
for wood in range(1, max(LOG)+1):
    m = 0
    for j in LOG:
        valid, remain = divmod(j, wood)

        if remain:
            used = valid * C
        else:
            used = (valid-1) * C

        temp = valid * W * wood - used

        if temp < 0:
            continue

        m += temp
    if m >= max_m:
        max_m = m
print(max_m)