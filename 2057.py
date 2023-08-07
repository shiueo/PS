import sys
import math

N = int(sys.stdin.readline())

if N == 0:
    print('NO')
else:
    l = [math.factorial(i) for i in range(19, -1, -1)]

    for k in l:
        if k <= N:
            N -= k

    if N:
        print("NO")
    else:
        print('YES')