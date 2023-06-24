import sys

S = sys.stdin.readline().strip()

while 'WUB' in S:
    S = S.replace('WUB', ' ')

print(' '.join(S.split()))