import sys

a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))

k = []
for i in c:
    if i < b:
        k.append(str(i))
print(" ".join(k))
