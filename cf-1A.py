import sys

n,m,a = map(int, sys.stdin.readline().split())

import math

print(math.ceil(n/a)*math.ceil(m/a))