import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

m_p = 0
start = L[0]
for i in range(N):
    tmp = L[i]
    pow = 0
    while tmp % 3 == 0:
        tmp //= 3
        pow+=1
    if pow > m_p or pow == m_p and L[i] < start:
        m_p = pow
        start = L[i]
res = [start]

for i in range(N):
    if res[-1] * 2 in L:
        res.append(res[-1] * 2)
        continue
    if res[-1] % 3 == 0 and res[-1] // 3 in L:
        res.append(res[-1]//3)
        continue

print(*res)
