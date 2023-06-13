import sys

sys.stdin.readline()
l = list(map(int, sys.stdin.readline().strip().split()))

print(min(l) * max(l))
