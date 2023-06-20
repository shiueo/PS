import sys

N = int(sys.stdin.readline())
fibo = [0 for i in range(N)]
if N >= 2:
    fibo[0] = 1
    fibo[1] = 1
    for i in range(2, N):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    print(fibo[-1])
else:
    if N == 1:
        print("1")
    else:
        print("0")
