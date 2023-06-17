import sys

N = int(sys.stdin.readline())

res = N
for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        while N % i == 0:
            N = N // i

        res -= res / i

if N > 1:
    res -= res / N
print(int(res))
