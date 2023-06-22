import sys

x = sys.stdin.readline().strip().split('-')

res = ''
for i in x:
    res += i[0]
print(res)
