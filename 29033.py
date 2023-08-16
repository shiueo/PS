import sys

a, b, c, d, e, f, g, h, i, j = map(int, sys.stdin.readline().split())

for x in range(a + 1):
    first = x
    second = a - x
    third = b - x
    fourth = c - x
    fifth = d - x

    if first < 0 or second < 0 or third < 0 or fourth < 0 or fifth < 0:
        continue
    if not e == second + third:
        continue
    if not f == second + fourth:
        continue
    if not g == second + fifth:
        continue
    if not h == third + fourth:
        continue
    if not i == third + fifth:
        continue
    if not j == fourth + fifth:
        continue

    print("YES")
    sys.exit()
print("NO")
