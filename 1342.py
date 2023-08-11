from collections import Counter
import sys

X = list(map(str, sys.stdin.readline().strip()))
c = Counter(X)


def isitlucky(prev_w, curr_l):
    count = 0
    if curr_l == len(X):
        return 1
    for i in c.keys():
        if i == prev_w or c[i] == 0:
            continue
        c[i] -= 1
        count += isitlucky(i, curr_l + 1)
        c[i] += 1
    return count


print(isitlucky('', 0))
