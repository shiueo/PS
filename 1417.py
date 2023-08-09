import sys

N = int(sys.stdin.readline())
my_n = int(sys.stdin.readline())
L = []
if N > 1:
    for i in range(N - 1):
        L.append(int(sys.stdin.readline()))
    c = 0
    L.sort(reverse=True)
    while L[0] >= my_n:
        L[0] -= 1
        c += 1
        my_n += 1
        L.sort(reverse=True)
    print(c)
else:
    print(0)
