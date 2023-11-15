import sys

N = int(sys.stdin.readline())

if N == 0:
    print(0)
else:
    fibo = [0 for i in range(N + 1)]
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, N + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2])%1000000007
    print(fibo[-1])
