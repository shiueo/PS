import sys

X = sys.stdin.readline().strip()

D = dict()
for i in X:
    if i not in D:
        D[i] = 1
    else:
        D[i] += 1

keys = sorted(D.keys())
odd_char = ""
c = 0
for key in keys:
    if D[key] % 2 == 1:
        odd_char = key
        c += 1
    if c >= 2:
        print("I'm Sorry Hansoo")
        sys.exit()

res = ""
temp = ""
for key in keys:
    count = D[key] // 2
    temp += key * count
    D[key] = D[key] // 2
res += temp
if odd_char != "":
    res += odd_char
res += temp[::-1]

print(res)
