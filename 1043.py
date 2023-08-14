import sys

N, M = map(int, sys.stdin.readline().split())
real = list(map(int, sys.stdin.readline().split()))
parties = [set(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(M)]

if len(real) != 1:
    real = real[1:]
else:
    print(M)
    sys.exit()
c = 0
real = set(real)

for i in range(len(parties)):
    for j in range(len(parties)):
        if real & parties[j]:
            real |= parties[j]

c = 0
for party in parties:
    if not party & real:
        c += 1
print(c)
