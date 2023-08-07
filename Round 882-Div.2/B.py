import sys

TEST_CASES = int(sys.stdin.readline())
for _ in range(TEST_CASES):
    n = int(sys.stdin.readline())
    strengths = list(map(int, sys.stdin.readline().split()))

    min_strength = strengths[0]
    max_groups = 1

    for i in range(1, n):
        if strengths[i] < min_strength:
            min_strength = strengths[i]
            print(i, 'irrer', min_strength)
            max_groups += 1
        else:
            min_strength &= strengths[i]
            print(i, 'uwuw', min_strength)

    print(max_groups)

