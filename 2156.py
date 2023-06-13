import sys

N = int(sys.stdin.readline())
L = []
for i in range(N):
    L.append(int(sys.stdin.readline()))

MOD = 10000003

"""
연속 3잔을 못 마심
->DP
"""

dp = [0 for _ in range(N)]

"""경우의 수
3잔
마지막 잔을 고른다고 해보면

1 2 3 4 5 
-> 3 4 5 = 12 max

마지막 잔 전 거를 안 마셨으면 그 전거를 고를 수 있고
마지막 잔 전거를 먹었으면 그 전거를 못 먹고 그 전 전 거를 먹었을 거다
근데 그 전거도 안 먹으면
:thinking:
그냥 n n-1비교
"""

if N == 1:
    print(L[0])
elif N == 2:
    print(L[0]+L[1])
elif N == 3:
    print(max(L[0]+L[1], L[1]+L[2], L[0]+L[2]))
else:
    dp[0] = L[0]
    dp[1] = L[0]+L[1]
    dp[2] = max(L[0]+L[1], L[1]+L[2], L[0]+L[2])
    for i in range(3, N):
        dp[i] = max(dp[i-3] + L[i] + L[i-1], dp[i-2] + L[i])
        dp[i] = max(dp[i-1], dp[i])

    print(dp[-1])


