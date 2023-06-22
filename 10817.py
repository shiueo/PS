import sys


n = list(map(int, sys.stdin.readline().split()))
n.sort()
print(n[1])
