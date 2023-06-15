"""이거도 dp

한번에 한 계단 또는 두 계단 오를 수 있음
연속된 세 계단을 밟아서는 안됨

마지막 계단은 무조건 밟아야함
-> 항상 마지막계단으로 보고 올라가면 됨
"""
import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0 for _ in range(N)]

if N <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    print(dp[-1])
