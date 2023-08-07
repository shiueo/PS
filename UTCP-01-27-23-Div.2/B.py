import sys

n = int(sys.stdin.readline())
s = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

L.sort()

sd = 0
for i in L:
    sd += i
    if sd > s:
        sd -= i
        break

print(sd)