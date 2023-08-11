import sys

N = int(sys.stdin.readline())
TREE_MAKING = list(map(int, sys.stdin.readline().split()))
to_del = int(sys.stdin.readline())


def DEL_NODE(toDel):
    TREE_MAKING[toDel] = -2
    for i in range(len(TREE_MAKING)):
        if toDel == TREE_MAKING[i]:
            DEL_NODE(i)


DEL_NODE(to_del)
cnt = 0
for i in range(len(TREE_MAKING)):
    if TREE_MAKING[i] != -2 and i not in TREE_MAKING:
        cnt += 1
print(cnt)
