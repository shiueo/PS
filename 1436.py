import sys

N = int(sys.stdin.readline())

sixsixsix = 0
n = 0
while 1:
    n += 1
    if '666' in str(n):
        sixsixsix+=1
    if sixsixsix == N:
        break
print(n)
