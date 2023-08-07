import sys


def get_position(h: int):
    return (h-1) // 4, (h-1) % 4


n1, n2 = map(int, sys.stdin.readline().split())
x1, y1 = get_position(n1)
x2, y2 = get_position(n2)
print(abs(x2 - x1) + abs(y2 - y1))
