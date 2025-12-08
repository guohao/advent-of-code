from util import *

r = {x: 0 for x in "abcd"}
r["a"] = 7


def value_of(n: str):
    if n in "abcd":
        return r[n]
    return int(n)


i = 0
while i < R:
    op, *opr = L[i].split()
    if len(opr) == 1:
        a = opr[0]
        b = None
    else:
        a, b = opr
    if "cpy" == op:
        if b in "abcd":
            r[b] = value_of(a)
    elif "inc" == op:
        r[a] += 1
    elif "dec" == op:
        r[a] -= 1
    elif "tgl" in op:
        t = value_of(a) + i
        if 0 <= t < R:
            tc = L[t].split()
            if len(tc) == 2:
                if tc[0] == "inc":
                    L[t] = f"dec {tc[1]}"
                else:
                    L[t] = f"inc {tc[1]}"
            elif len(tc) == 3:
                if tc[0] == "jnz":
                    L[t] = f"cpy {tc[1]} {tc[2]}"
                else:
                    L[t] = f"jnz {tc[1]} {tc[2]}"
            else:
                raise Exception(op)
    elif "jnz" == op:
        if value_of(a):
            i += value_of(b)
            continue
    else:
        raise Exception(op)

    i += 1
print(r["a"])

# transform from input manually
print(12 * math.prod(range(1, 12)) + 80 * 76)
