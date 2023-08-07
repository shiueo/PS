import sys

chain = []
N_1 = int(input())

index = 0
for i in range(N_1):
    kk = input().strip()
    if kk == "?":
        index = i
    chain.append(kk)
N_2 = int(input())
candidates = []
chain_set = set(chain)
for i in range(N_2):
    candidates.append(input().strip())

if N_1 == 1:
    print(candidates[0])
elif index == N_1 - 1:
    end_letter = chain[index - 1][-1]
    print(next((i for i in candidates if i[0] == end_letter and i not in chain_set), None))
elif index == 0:
    start_letter = chain[index + 1][0]
    print(next((i for i in candidates if i[-1] == start_letter and i not in chain_set), None))
else:
    end_letter = chain[index - 1][-1]
    start_letter = chain[index + 1][0]
    print(next((i for i in candidates if i[0] == end_letter and i[-1] == start_letter and i not in chain_set), None))
