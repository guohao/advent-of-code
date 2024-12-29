from util import *


def tick(a) -> bool:
    r = {x: 0 for x in 'abcd'}
    r['a'] = a

    def value_of(n: str):
        if n in r:
            return r[n]
        return int(n)

    i = 0
    c = cycle([0, 1])
    cnt = 0
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
            case 'out':
                if value_of(a) != next(c):
                    return False
                cnt += 1
                if cnt == 10:
                    return True
            case 'jnz':
                if value_of(a):
                    i += value_of(b)
                    continue
        i += 1
    return False


for k in count():
    if tick(k):
        print(k)
        break
