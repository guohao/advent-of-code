import math
import re
import sys

PS = sys.stdin.read().split("\n\n")
parts = PS
rules = parts[0].splitlines()


def calc(name, x, m, a, s):
    if name == "A":
        return x + m + a + s
    elif name == "R":
        return 0
    rule = [x for x in rules if x.split("{")[0] == name][0]
    content = rule[len(name) + 1 : -1]
    for item in content.split(","):
        cells = item.split(":")
        if len(cells) == 1 or eval(cells[0]):
            return calc(cells[-1], x, m, a, s)


ans = 0
for line in parts[1].splitlines():
    d = list(map(int, re.findall(r"\d+", line)))
    ans += calc("in", *d)
print(ans)


def calc2(name, d):
    if name == "R":
        return 0
    if name == "A":
        return math.prod(map(len, d.values()))
    rule = [x for x in rules if x.split("{")[0] == name][0]
    content = rule[len(name) + 1 : -1]
    ans = 0
    for item in content.split(","):
        cells = item.split(":")
        target = cells[-1]
        if len(cells) == 1:
            ans += calc2(target, d)
            break
        else:
            k = cells[0][0]
            expr = cells[0].replace(k, "v")
            md = d.copy()
            md[k] = [v for v in d[k] if eval(expr)]
            ans += calc2(target, md)
            d[k] = [v for v in d[k] if not eval(expr)]
    return ans


print(calc2("in", {x: list(range(1, 4001)) for x in "xmas"}))
