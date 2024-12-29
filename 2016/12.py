from util import *


def f(p2=None):
    r = {x: 0 for x in 'abcd'}
    i = 0

    def value_of(n: str):
        if n in r:
            return r[n]
        return int(n)

    if p2:
        r['c'] = 1
    while i < R:
        op, *opr = L[i].split()
        if len(opr) == 1:
            a = opr[0]
            b = None
        else:
            a, b = opr
        match op:
            case 'cpy':
                r[b] = value_of(a)
            case 'inc':
                r[a] += 1
            case 'dec':
                r[a] -= 1
            case 'jnz':
                if value_of(a):
                    i += value_of(b)
                    continue
        i += 1
    print(r['a'])


f()
f(1)
