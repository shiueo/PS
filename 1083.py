import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

# 움직일 수 있는 범위 내에서 가장 큰수를 찾아서 걔를 왼쪽으로 일단 밀고 옮겨가면서 밀자
cnt = 0
current_index = 0
while 1:
    if current_index == len(L)-1:
        break
    if current_index + S + 1 <= len(L):
        last_p = current_index + S + 1
    else:
        last_p = len(L)
    partial_max_index = L.index(max(L[current_index:last_p]))
    if partial_max_index == current_index:
        current_index += 1
    else:
        S -= partial_max_index - current_index
        L = L[:current_index] + [L[partial_max_index]] + L[current_index:partial_max_index] + L[partial_max_index+1:]
        current_index += 1
    if S == 0:
        break
print(*L)
