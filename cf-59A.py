import sys

x = sys.stdin.readline().strip()

low = 0
cap = 0
for i in x:
    if i == i.lower():
        low += 1
    else:
        cap += 1

if low >= cap:
    print(x.lower())
else:
    print(x.upper())
