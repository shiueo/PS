import sys

x = sys.stdin.readline().strip()

D = ['h', 'e', 'l', 'l', 'o']
D.reverse()

for i in x:
    if i == D[-1]:
        D.pop()
    if len(D) == 0:
        break

if len(D) == 0:
    print("YES")
else:
    print('NO')
