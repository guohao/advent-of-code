from util import *

tt = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

e = {}
for line in tt.splitlines():
    l, v = line.split(": ")
    e[l] = int(v)

a = {}
for line in L:
    vs = ints(line)
    a[vs[0]] = dict(zip(re.findall(r'([a-z]+):', line), vs[1:]))

for i, v in a.items():
    if all(e[k] == v[k] for k in v):
        print(i)
        break
for i, v in a.items():
    for k in v:
        if k in ['cats', 'trees']:
            if v[k] <= e[k]:
                break
        elif k in ['pomeranians', 'goldfish']:
            if v[k] >= e[k]:
                break
        else:
            if v[k] != e[k]:
                break
    else:
        print(i)
        break
