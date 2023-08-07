import sys

N = int(sys.stdin.readline())

i = 1
while i < N:
    N -= i
    i += 1

if i % 2:
    numerator = i-N+1
    denominator = N
else:
    numerator = N
    denominator = i-N+1
print(f"{numerator}/{denominator}")
