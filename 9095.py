"""dp같다


N+1의 수는 전 수를 표현하는 방식에서 1 2 3 을 더하는 것으로 볼 수 있다

1   2   3   4
1   2   4   7
"""
import sys

N = int(sys.stdin.readline())
for i in range(N):
    J = int(sys.stdin.readline())
    dp = [0 for _ in range(J)]

    if J > 3:
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        for j in range(4, J):
            dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

        print(dp[-1])
    else:
        dp = [1,2,4]
        print(dp[J - 1])
