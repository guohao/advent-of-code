from util import *
from z3 import *

a, b, c, *prog = map(int, re.findall(r"\d+", RAW))
output = []
i = 0

while i < len(prog) - 1:
    V = {i: i for i in range(4)}
    V[4] = a
    V[5] = b
    V[6] = c

    op = prog[i + 1]
    match prog[i]:
        case 0:
            a >>= V[op]
        case 1:
            b ^= op
        case 2:
            b = 7 & V[op]
        case 3:
            i = op - 2 if a else i
        case 4:
            b ^= c
        case 5:
            output.append(V[op] & 7)
        case 6:
            b = a >> V[op]
        case 7:
            c = a >> V[op]
    i += 2

print(output)

outs = list(map(int, re.findall(r"\d+", L[-1])))

s = Optimize()
a = BitVec("a", 64)
s.add(a > 0)
a_vars = [a]
expect = [BitVec(f"e_{i}", 64) for i in range(len(outs))]

for i in range(len(outs)):
    s.add(expect[i] == BitVecVal(outs[i], 64))
    ai = a_vars[i]
    a_low = ai & BitVecVal(7, 64)
    shift_amount = a_low ^ BitVecVal(5, 64)
    ai_shifted = LShR(ai, shift_amount)
    expr = ai_shifted ^ a_low
    expr = expr ^ BitVecVal(3, 64)
    b = expr & BitVecVal(7, 64)
    s.add(expect[i] == b)
    a_next = BitVec(f"a_{i + 1}", 64)
    s.add(a_next == LShR(ai, 3))
    a_vars.append(a_next)
s.minimize(a)
s.check()
print(s.model()[a])
