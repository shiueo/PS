import sys

N = sys.stdin.readline().strip()

count = 0
cache_N = int(N)
if len(N) == 1:
    N = f"0{N}"
while 1:
    N = f"{N[-1]}{str(int(N[0]) + int(N[1]))[-1]}"
    count += 1
    if int(N) == cache_N:
        break
print(count)
