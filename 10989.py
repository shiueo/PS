import sys

N = [0] * 10000

k = int(sys.stdin.readline())

for i in range(k):
    N[int(sys.stdin.readline()) - 1] += 1

for i in range(1, 10001):
    if N[i - 1] > 0:
        for j in range(N[i - 1]):
            print(i)
