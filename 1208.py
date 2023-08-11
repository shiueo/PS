import sys
N, S = map(int, sys.stdin.readline().split())

L = list(map(int, sys.stdin.readline().split()))

L_DICT = dict()
R_DICT = dict()

mid = len(L) // 2


def BackTrack(subseq, l, sum_p, index, target_dict):
    if sum_p in target_dict.keys():
        target_dict[sum_p] += 1
    else:
        target_dict[sum_p] = 1

    for i in range(index, len(l)):
        next_l = subseq + [l[i]]
        next_sum = sum_p + l[i]
        BackTrack(next_l, l, next_sum, i + 1, target_dict)
        next_l.pop()


BackTrack([], L[:mid], 0, 0, L_DICT)
BackTrack([], L[mid:], 0, 0, R_DICT)
c = 0
for lp in L_DICT.keys():
    if S - lp in R_DICT.keys():
        c += L_DICT[lp] * R_DICT[S - lp]

if S == 0:
    print(c - 1)
else:
    print(c)
