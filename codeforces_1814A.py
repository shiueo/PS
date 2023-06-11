import sys

n = int(sys.stdin.readline())
for i in range(n):
    u, k = map(int, sys.stdin.readline().strip().split())
    if u % 2 == 0:
        print("YES")
    else:
        if u >= k and k % 2 == 1:
            print("YES")
        else:
            print('NO')