import sys

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    res = []
    for j in range(1, num + 1):
        res.append(str(j * 2))

    print(" ".join(res))
