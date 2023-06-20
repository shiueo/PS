import sys

x = int(sys.stdin.readline())

res = 0
for i in [5, 4, 3, 2, 1]:
    res += x // i
    x %= i
print(res)
