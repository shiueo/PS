import sys

N = int(sys.stdin.readline())
BRIDGE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in BRIDGE:
    i[2] -= 1
BRIDGE.sort()
pillar = 0
for i in range(len(BRIDGE)):
    left_pillar, right_pillar = BRIDGE[i][0], BRIDGE[i][0]
    for j in range(i - 1, -1, -1):
        # LEFT
        if BRIDGE[j][1] <= BRIDGE[i][1] <= BRIDGE[j][2]:
            left_pillar -= BRIDGE[j][0]
            break
    for j in range(i - 1, -1, -1):
        # RIGHT
        if BRIDGE[j][1] <= BRIDGE[i][2] <= BRIDGE[j][2]:
            right_pillar -= BRIDGE[j][0]
            break
    pillar += left_pillar + right_pillar

print(pillar)
