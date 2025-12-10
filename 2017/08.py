from collections import defaultdict
import sys

L = sys.stdin.readlines()
rs = defaultdict(int)
ans = 0
for line in L:
    cells = line.split()
    reg, op, val, _, cond_reg, cond_op, cond_val = cells
    val = int(val)
    cond_val = int(cond_val)

    cond_met = False
    if cond_op == ">":
        cond_met = rs[cond_reg] > cond_val
    elif cond_op == "<":
        cond_met = rs[cond_reg] < cond_val
    elif cond_op == ">=":
        cond_met = rs[cond_reg] >= cond_val
    elif cond_op == "<=":
        cond_met = rs[cond_reg] <= cond_val
    elif cond_op == "==":
        cond_met = rs[cond_reg] == cond_val
    elif cond_op == "!=":
        cond_met = rs[cond_reg] != cond_val

    if cond_met:
        if op == "inc":
            rs[reg] += val
        else:
            rs[reg] -= val
        ans = max(ans, max(rs.values()))

print(max(rs.values()))
print(ans)
