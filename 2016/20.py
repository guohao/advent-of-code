from util import *

rules = sorted([ints(l, neg=False) for l in L], key=lambda x: x[1])

ip = 0
c = 0
first = None
while ip <= 4294967295:
    for i in range(len(rules)):
        r = rules[i]
        if r[0] <= ip <= r[1]:
            ip = r[1] + 1
            break
    else:
        if not first:
            first = ip
            print(ip)
        ip += 1
        c += 1

print(c)
