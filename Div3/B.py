import sys

test_cases = int(sys.stdin.readline())
for _ in range(test_cases):
    first_line = list(sys.stdin.readline().strip())
    second_line = list(sys.stdin.readline().strip())
    third_line = list(sys.stdin.readline().strip())
    full = [first_line, second_line, third_line]

    valid = False
    for i in range(3):
        if full[i][0] == full[i][1] == full[i][2] and full[i][2] != '.':
            print(full[i][0])
            valid = True
            break

    for i in range(3):
        if full[0][i] == full[1][i] == full[2][i] and full[0][i] != '.':
            print(full[0][i])
            valid = True
            break

    if full[0][0] == full[1][1] == full[2][2] and full[0][0] != '.':
        print(full[0][0])
        valid = True

    if full[1][1] == full[0][2] == full[2][0] and full[1][1] != '.':
        print(full[1][1])
        valid = True

    if not valid:
        print("DRAW")
