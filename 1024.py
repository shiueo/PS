import sys

N, L = map(int, sys.stdin.readline().split())

for i in range(L, 101):
    F = N - (i * (i + 1) / 2)

    if F % i == 0:
        F = int(F / i)
        if F >= -1:
            print(' '.join([str(_) for _ in range(F + 1, F + i + 1)]))
            break
else:
    print(-1)
