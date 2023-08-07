import sys

N = int(sys.stdin.readline())

jobs = set()
for i in range(N):
    jobs.add(sys.stdin.readline().strip())

what_i_did = int(sys.stdin.readline())
what_i_did_jobs = set()
for i in range(what_i_did):
    what_i_did_jobs.add(sys.stdin.readline().strip())

what_i_can_do = jobs - what_i_did_jobs

if len(what_i_can_do) > 0:
    print(len(what_i_can_do))
    for i in what_i_can_do:
        print(i)
else:
    print(0)