from util import *

prog = L


def f(p2=None):
    pc = 0
    r = {'a': 0, 'b': 0}
    if p2:
        r['a'] = 1
    while pc < len(prog):
        i = prog[pc]
        if 'hlf' in i:
            r[i.split()[-1]] //= 2
        elif 'tpl' in i:
            r[i.split()[-1]] *= 3
        elif 'inc' in i:
            r[i.split()[-1]] += 1
        elif 'jmp' in i:
            pc += int(i.split()[-1])
            continue
        elif 'jie' in i:
            if r[i[4]] % 2 == 0:
                pc += int(i.split()[-1])
                continue
        elif 'jio' in i:
            if r[i[4]] == 1:
                pc += int(i.split()[-1])
                continue
        else:
            raise Exception(i)
        pc += 1
    print(r['b'])


f()
f(1)
