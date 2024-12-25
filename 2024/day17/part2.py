import re
from z3 import *

outs = list(map(int, re.findall(r'\d+', sys.stdin.readlines()[-1])))

s = Optimize()
a = BitVec('a', 64)
s.add(a > 0)
a_vars = [a]
expect = [BitVec(f'e_{i}', 64) for i in range(len(outs))]

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
    a_next = BitVec(f'a_{i + 1}', 64)
    s.add(a_next == LShR(ai, 3))
    a_vars.append(a_next)
s.minimize(a)
s.check()
print(s.model().evaluate(a).as_long())
