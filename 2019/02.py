from util import *

ns = [int(x) for x in D.split(',')]
ns[1] = 12
ns[2] = 2
i = 0
while True:
    if ns[i] == 99:
        break
    if ns[i] == 1:
        ns[ns[i + 3]] = ns[ns[i + 1]] + ns[ns[i + 2]]
    else:
        ns[ns[i + 3]] = ns[ns[i + 1]] * ns[ns[i + 2]]
    i += 4
print(ns[0])

on = [int(x) for x in D.split(',')]

for n, v in product(range(99), repeat=2):
    ns = on.copy()
    ns[1] = n
    ns[2] = v
    i = 0
    while True:
        if ns[i] == 99:
            break
        if ns[i] == 1:
            ns[ns[i + 3]] = ns[ns[i + 1]] + ns[ns[i + 2]]
        else:
            ns[ns[i + 3]] = ns[ns[i + 1]] * ns[ns[i + 2]]
        i += 4
    if ns[0] == 19690720:
        print(n * 100 + v)
        break
