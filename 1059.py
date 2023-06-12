import sys

sys.stdin.readline()
S = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

"""
A와 B는 양의 정수이고 A<B
A<=x<=B를 만족하는 모든 정수 x가 집합 S에 포함되지 않을 때 이를 좋은 집합이라 함

구하는거: 좋은 집합의 수
"""

if N in S:
    print(0)

else:
    S.append(0)
    S.sort()

    i = 0
    for i in range(len(S)):
        if S[i] > N:
            break

    print((N-(S[i-1]+1))*(S[i]-N) + (S[i]-N-1))
