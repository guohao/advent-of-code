from collections import deque
import sys

import re

sys.path.insert(0, "..")
from util import *

t = 0
for line in L:
    line = line.strip()
    operands = deque()
    operators = deque()
    for c in line.replace("(", "( ").replace(")", " )").split():
        if c.isdigit():
            operands.append(c)
        elif c == "(":
            operators.append(c)
        elif c == ")":
            while operators and operators[-1] != "(":
                operands.append(
                    eval(f"{operands.pop()} {operators.pop()} {operands.pop()}")
                )
            operators.pop()
        else:
            while operators and operators[-1] != "(":
                operands.append(
                    eval(f"{operands.pop()} {operators.pop()} {operands.pop()}")
                )
            operators.append(c)
    while operators:
        operands.append(eval(f"{operands.pop()} {operators.pop()} {operands.pop()}"))
    t += operands.pop()
print(t)

t = 0
for line in L:
    line = line.strip()
    operands = deque()
    operators = deque()
    precedence = {"+": 1, "*": 0}
    for c in line.replace("(", "( ").replace(")", " )").split():
        if c.isdigit():
            operands.append(c)
        elif c == "(":
            operators.append(c)
        elif c == ")":
            while operators and operators[-1] != "(":
                operands.append(
                    eval(f"{operands.pop()} {operators.pop()} {operands.pop()}")
                )
            operators.pop()
        else:
            while (
                operators
                and operators[-1] != "("
                and precedence[c] <= precedence[operators[-1]]
            ):
                operands.append(
                    eval(f"{operands.pop()} {operators.pop()} {operands.pop()}")
                )
            operators.append(c)
    while operators:
        operands.append(eval(f"{operands.pop()} {operators.pop()} {operands.pop()}"))
    t += operands.pop()

print(t)
