"""
3의 제곱수의 합
-> 3진법? 그러나 2진법

0 -> 0
10 -> 1
11 -> 4
100 -> 9

n을 2진법으로 바꾸고 3진법으로 바꿈
"""
import sys

print(int(bin(int(sys.stdin.readline()))[2:], 3))
