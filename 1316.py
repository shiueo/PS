import sys

N = int(sys.stdin.readline())
o = 0
for i in range(N):
    K = sys.stdin.readline().strip()
    c = K[0]
    u = [c]
    for j in K:
        if j != c:
            u.append(j)
            c = j
    if len(set(u)) == len(u):
        o += 1

print(o)
