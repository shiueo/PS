a = input()
c = list(map(int, input().split()))
k = int(input())

s=0
for i in c:
    if i == k:
        s+=1

print(s)