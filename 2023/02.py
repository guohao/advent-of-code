from collections import defaultdict
import math
import re
import sys


def join(l):
    return "".join(map(str, l))


pattern = "|".join(r"\d+ " + x for x in ["blue", "green", "red"])


def f(p2=None):
    t = 0
    for line in L:
        cells = line.split(":")
        if p2:
            c_max = defaultdict(int)
        else:
            c_max = {"blue": 14, "green": 13, "red": 12}

        i = int(re.findall(r"-?\d+", cells[0])[0])
        for cnt, color in map(str.split, re.findall(pattern, cells[1])):
            if p2:
                c_max[color] = max(c_max[color], int(cnt))
            else:
                if c_max[color] < int(cnt):
                    break
        else:
            if not p2:
                t += i
        if p2:
            t += math.prod(c_max.values())
    print(t)


f()
f(1)
