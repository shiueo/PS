import sys

POLY = sys.stdin.readline().strip()

POLY_SPLITTED = []
for i in POLY.split("."):
    if i:
        POLY_SPLITTED.append(i)

RES = ""
for i in POLY_SPLITTED:
    if len(i) % 2 == 0:
        RES += "AAAA" * (len(i) // 4)
        RES += "BB" * (len(i) % 4 // 2)
    else:
        print("-1")
        sys.exit()

K = []
j = 0
for i in range(len(POLY)):
    if POLY[i] == ".":
        K.append(".")
    else:
        K.append(RES[j])
        j += 1
print("".join(K))
