from util import *

prog = L


def f(p2=None):
    pc = 0
    r = {'a': 0, 'b': 0}
    if p2:
        r['a'] = 1
    while pc < len(prog):
        op, *opr = prog[pc].replace(',', '').split()
        if len(opr) == 1:
            a = opr[0]
            b = None
        else:
            a, b = opr
        match op:
            case 'hlf':
                r[a] //= 2
            case 'tpl':
                r[a] *= 3
            case 'inc':
                r[a] += 1
            case 'jmp':
                pc += int(a)
                continue
            case 'jie':
                if r[a] % 2 == 0:
                    pc += int(b)
                    continue
            case 'jio':
                if r[a] == 1:
                    pc += int(b)
                    continue
        pc += 1
    print(r['b'])


f()
f(1)
