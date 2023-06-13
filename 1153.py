"""
Goldbach?

에라토스테네스 체
"""
import sys


def get_prime(n):
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return a


N = int(sys.stdin.readline())
"""
1 -> x
2 -> x
3 -> x
4 -> x
5 -> x
6 -> x
7 -> x
8 -> 2+2+2+2
9 -> 2 + 2 + 2 + 3
"""

answer = []
if N >= 8:
    if N % 2 == 1:
        answer.append(2)
        answer.append(3)
        N -= 5
    else:
        answer.append(2)
        answer.append(2)
        N -= 4

    primes = get_prime(N)
    for i in range(2, N + 1):
        if primes[i] and primes[N - i]:
            answer.append(i)
            answer.append(N - i)
            break
    print(" ".join(list(map(str, answer))))
else:
    print("-1")
