import sys


def Eratosthenes(N):
    sieve = [True] * (N + 1)
    sieve[0] = False
    sieve[1] = False
    until = int(N ** 0.5)
    for i in range(until + 1):
        if sieve[i]:
            for j in range(2 * i, N + 1, i):
                sieve[j] = False
    return [i for i in range(N + 1) if sieve[i]]


def factorization(x):
    cnt = 0
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            cnt += 1
            x = x / i
    if x != 1:
        cnt += 1
    return cnt


A, B = map(int, sys.stdin.readline().split())

targets = Eratosthenes(B)
targets_set = set(targets)

cc = 0
for i in range(A, B + 1):
    count = 0
    k = factorization(i)
    if k in targets_set:
        cc += 1
print(cc)
