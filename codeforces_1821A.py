import sys

n = int(sys.stdin.readline())

for i in range(n):
    stt = list(sys.stdin.readline().strip())

    c = 1
    if stt[0] == '0':
        print("0")
    else:
        for k in range(len(stt)):
            if k == 0:
                if stt[k] == '?':
                    c *= 9
                else:
                    c *= 1
            else:
                if stt[k] == '?':
                    c *= 10
                else:
                    c *= 1
        print(c)
