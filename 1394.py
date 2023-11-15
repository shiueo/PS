import sys

S = sys.stdin.readline().strip()
pw = sys.stdin.readline().strip()
D = dict()

c = 1
for i in S:
    D[i] = c
    c += 1

len_S = len(S)
t = 0
for i in range(len(pw)):
    t *= len_S
    t += D[pw[i]]
    t %= 900528
print(t)
