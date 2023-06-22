import sys

N = int(sys.stdin.readline())
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

length = 1
for i in range(len(str(N))):
    new = int(str(N // 10) + "9")
    R = new - N

    for j in range(10):
        nums[j] += (N // 10 + 1) * length
    for j in range(10 - R, 10):
        nums[j] -= length
    for number in list(str(N)[:-1]):
        nums[int(number)] -= R * length
    nums[0] -= length

    N //= 10
    length *= 10

print(' '.join(map(str, nums)))
