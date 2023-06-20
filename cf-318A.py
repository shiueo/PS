"""
1 3 5 7 9 2 4 6 8 10
1 3 5 7 2 4 6
"""
import sys

a, b = map(int, sys.stdin.readline().split())

if b > (a+1) // 2:
    print(2*(b - ((1+a)//2)))
else:
    print(2*b-1)
