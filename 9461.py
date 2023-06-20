import sys

X = [0 for i in range(101)]

X[1] = 1
X[2] = 1
X[3] = 1

for i in range(4, 101):
    X[i] = X[i - 3] + X[i - 2]

n = int(sys.stdin.readline())
for i in range(n):
    u = int(sys.stdin.readline())
    print(X[u])
