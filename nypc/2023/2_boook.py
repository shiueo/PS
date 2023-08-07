import sys

N, M = map(int, sys.stdin.readline().split())


def split_text_without_cutting_words(text, length):
    words = text.split()
    result = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            result.append(current_line)
            current_line = word

    if current_line:
        result.append(current_line)

    return result


contents = []
for i in range(N):
    data = sys.stdin.readline().strip()
    for j in split_text_without_cutting_words(data, M):
        if j:
            contents.append(j)
res = []
center = 0
right = 0
for cont in contents:
    if cont == '<CENTER>':
        center = 1
        continue
    if cont == '</CENTER>':
        center = 0
        continue
    if cont == '<RIGHT>':
        right = 1
        continue
    if cont == '</RIGHT>':
        right = 0
        continue

    if center == 1:
        res.append(cont.center(M, '-').replace(' ', '-'))
        continue

    if right == 1:
        res.append(cont.rjust(M, '-').replace(' ', '-'))
        continue

    res.append(cont.ljust(M, '-').replace(' ', '-'))

print('\n'.join(res))