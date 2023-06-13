"""
S = A[0] × B[0] + ... + A[N-1] × B[N-1]
"""
import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

s = 0
for i in range(N):
    s += A[i] * B[i]

print(s)
