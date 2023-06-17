import sys

N = int(sys.stdin.readline())
D = dict()
for i in range(N):
    A, B = sys.stdin.readline().strip().split()
    if A not in D:
        D[A] = int(B)
    else:
        D[A] = D[A] + int(B)

if 5 in D.values():
    print('YES')
else:
    print('NO')
