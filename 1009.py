n = int(input())

for i in range(n):
    k, m = map(int, input().split())
    k %= 10

    if k == 1:
        print(1)
    elif k == 2:
        u = [6, 2, 4, 8]
        print(u[m % 4])
    elif k == 3:
        u = [1, 3, 9, 7]
        print(u[m % 4])
    elif k == 4:
        u = [6, 4]
        print(u[m % 2])
    elif k == 5:
        print(5)
    elif k == 6:
        print(6)
    elif k == 7:
        u = [1, 7, 9, 3]
        print(u[m % 4])
    elif k == 8:
        u = [6, 8, 4, 2]
        print(u[m % 4])
    elif k == 9:
        u = [1, 9]
        print(u[m % 2])
    else:
        print(10)
