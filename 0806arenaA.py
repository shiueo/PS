a = dict()
for i in range(5):
    inn = input()
    if inn not in a:
        a[inn] = 1
    else:
        a[inn] += 1

for i in a.keys():
    if a[i] % 2 == 1:
        print(i)
