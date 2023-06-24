import sys

N = int(sys.stdin.readline())
i = 1
m = 2
while i <= N:
    i *= m

print(i//2)
