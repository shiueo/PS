"""
64
64
32
16 16
8 16
4 16
2 1
"""
import sys

sticks = [64, 32, 16, 8, 4, 2, 1]

N = int(sys.stdin.readline())
c = 0
for i in sticks:
    if N >= i:
        c += 1
        N -= i
    if N == 0:
        break

print(c)
