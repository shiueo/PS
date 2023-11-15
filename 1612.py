import sys

N = int(sys.stdin.readline())
if N % 2 == 0 or N % 5 == 0:
    print(-1)
else:
    t = 0
    cnt = 0
    while 1:
        t = 10 * t % N + 1
        cnt += 1
        if t % N == 0:
            print(cnt)
            break
