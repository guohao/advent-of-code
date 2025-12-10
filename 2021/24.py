import math
import sys
import re
from z3 import *

L = sys.stdin.readlines()


def join(l):
    return "".join(map(str, l))


def f(p: int):
    s = Optimize()
    size = int(math.log2(10**14)) + 1
    digits = [BitVec(f"d_{i}", size) for i in range(14)]
    var = {r: BitVecVal(0, size) for r in "xyzw"}

    pos = 0
    for i, inst in enumerate(L):
        instr, a_name, *b = inst.split()
        a = var[a_name]
        if b:
            b = var[b[0]] if b[0] in var else BitVecVal(int(b[0]), size)
        c = BitVec(f"v_{i}", size)

        match instr:
            case "inp":
                c = digits[pos]
                pos += 1
            case "add":
                s.add(c == a + b)
            case "mul":
                s.add(c == a * b)
            case "mod":
                s.add(c == a % b)
            case "div":
                s.add(c == a / b)
            case "eql":
                s.add(c == If(a == b, BitVecVal(1, size), BitVecVal(0, size)))
        var[a_name] = c

    s.add([0 < d for d in digits])
    s.add([d < 10 for d in digits])
    s.add(var["z"] == 0)

    optimizer = [s.maximize, s.minimize][p]
    optimizer(sum((10**i) * d for i, d in enumerate(digits[::-1])))
    s.check()
    m = s.model()
    print("".join([str(m[d]) for d in digits]))


f(0)
f(1)
