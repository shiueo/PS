import sys

score = []

for line in sys.stdin:
    score.append(list(map(int, line.split())))

dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(len(score) + 1)]

for i in range(len(score)):
    for w in range(16):
        for b in range(16):
            if w + 1 <= 15:
                dp[i + 1][w + 1][b] = max(dp[i + 1][w + 1][b], dp[i][w][b] + score[i][0])

            if b + 1 <= 15:
                dp[i + 1][w][b + 1] = max(dp[i + 1][w][b + 1], dp[i][w][b] + score[i][1])

            dp[i + 1][w][b] = max(dp[i + 1][w][b], dp[i][w][b])

print(dp[len(score)][15][15])
