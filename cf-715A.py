import sys

N = int(sys.stdin.readline())
res = []
for i in range(N):
    if i % 2 == 0:
        res.append("I hate")
    else:
        res.append("I love")

print(' that '.join(res)+" it")