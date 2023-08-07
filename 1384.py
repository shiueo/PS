count = 1
while True:
    n = int(input())

    if n == 0:
        break

    name = []
    word = []

    for _ in range(n):
        n_w = input().split()
        name.append(n_w[0])
        word.extend(n_w[1:])

    print("Group", count)
    nasty = True
    for i, w in enumerate(word):
        if w == 'N':
            print(name[(i + 1) % n], "was nasty about", name[i // (n - 1)])
            nasty = False

    if nasty:
        print("Nobody was nasty")
    print("")
    count += 1
