import sys

L, R = map(str, sys.stdin.readline().split())

if len(L) != len(R):
    print(0)
else:
    count = 0
    for i in range(len(L)):
        if L[i] == R[i] == '8':
            count += 1
        if L[i] != R[i]:
            break
    print(count)
