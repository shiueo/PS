import sys

N = sys.stdin.readline().strip()

N = list(N)
N.sort(reverse=True)
print("".join(N))
