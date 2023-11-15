import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
M = list(map(str, sys.stdin.readline().split()))
M.sort()
for i in combinations(M, L):
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
        if L-(i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u')) >= 2:
            print("".join(i))
