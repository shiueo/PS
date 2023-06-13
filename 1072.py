import sys

X, Y = map(int, sys.stdin.readline().split())

"""
승률 계산

10, 8 이 주어졌다면

8/10 이므로 1판만 더해도 바뀐다
승률이 소수점을 버림 -> 

이분탐색?


    1 ≤ X ≤ 1,000,000,000
    0 ≤ Y ≤ X


"""

Z = int(Y * 100 // X)
if Z >= 99:
    print(-1)
else:
    left = 1
    right = X
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        tmp = (Y + mid) * 100 // (X + mid)
        if tmp <= Z:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    print(answer)
