import sys

import math

x_s, y_s = map(int, sys.stdin.readline().split())

x_e, y_e, dx, dy = map(int, sys.stdin.readline().split())


# x_s y_s가 정류장임

def get_distance(cx, cy, nx, ny):
    return ((cx - nx) ** 2 + (cy - ny) ** 2) ** 0.5


real_diff = math.gcd(dx, dy)
dx, dy = dx // real_diff, dy // real_diff
cur_distance = get_distance(x_e, y_e, x_s, y_s)
while 1:
    x_e += dx
    y_e += dy
    curr_distance = get_distance(x_e, y_e, x_s, y_s)
    if curr_distance > cur_distance:
        break
    else:
        cur_distance = curr_distance
print(x_e-dx, y_e-dy)
