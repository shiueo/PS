a, b, c, d, e = map(int, input().split())

start_num = min(a, b, c, d, e)

K = [a, b, c, d, e]
while 1:
    c = 0
    for i in K:
        if start_num % i == 0:
            c += 1
    if c >= 3:
        break
    else:
        start_num += 1

print(start_num)
