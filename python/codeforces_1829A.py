import sys

n = int(sys.stdin.readline())
CODEFORCES = 'codeforces'
for i in range(n):
    c=0
    inn = sys.stdin.readline().strip()
    for k in range(len(inn)):
        if inn[k] != CODEFORCES[k]:
            c+=1
    print(c)
