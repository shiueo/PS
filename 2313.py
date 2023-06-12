import sys

LINE_NO = int(sys.stdin.readline())

L = []
for i in range(LINE_NO):
    sys.stdin.readline()
    L.append(list(map(int, sys.stdin.readline().split())))

res = ""
s = 0
for i in L:
    m, m_start, m_end = i[0], 0, 0
    start, end = 0, 0
    for j in range(1, len(i)):
        if i[j] >= i[j - 1] + i[j]:
            start, end = j, j
        else:
            i[j] = i[j - 1] + i[j]
            end = j

        if i[j] > m:
            m = i[j]
            m_end, m_start = end, start

        elif i[j] == m and m_end - m_start > end-start:
            m = i[j]
            m_end, m_start = end, start
    res += f'{m_start + 1} {m_end + 1}\n'
    s += m

print(s)
print(res)
