def calculate_power(a, l, r):
    power = 0
    for i in range(l, r):
        power += abs(a[i] - a[i + 1])
    return power


def find_min_power(t, test_cases):
    for _ in range(t):
        n, k = map(int, test_cases[_][0].split())
        a = list(map(int, test_cases[_][1].split()))

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(len(dp)):
            print(dp[i])
        print('------')
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for l in range(i):
                    dp[i][j] = min(dp[i][j], dp[l][j - 1] + calculate_power(a, l, i))
                    for i in range(len(dp)):
                        print(dp[i])
                    print('------')

        print(dp[n][k])
        for i in range(len(dp)):
            print(dp[i])
        print('------')


# Example usage
test_cases = [
    [('4 2'), '1 3 5 2'],
    [('6 3'), '1 9 12 4 7 2']
]
find_min_power(2, test_cases)
