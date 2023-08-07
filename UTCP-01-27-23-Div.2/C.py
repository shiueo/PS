import sys

n, c_x, c_y, r = map(int, sys.stdin.readline().split())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

s=0
for i in L:
    if ((i[0]-c_x)**2 + (i[1]-c_y)**2)**0.5 <= r:
        s+=1
print(s)