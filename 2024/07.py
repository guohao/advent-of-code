from util import *

t = 0
for ns in NS:
    for c in product(["+", "*"], repeat=len(ns) - 2):
        s = ns[1]
        for i in range(len(c)):
            if c[i] == "+":
                s += ns[i + 2]
            else:
                s *= ns[i + 2]
        if s == ns[0]:
            t += ns[0]
            break
print(t)
t = 0
for ns in NS:
    for c in product(["+", "*", "||"], repeat=len(ns) - 2):
        s = ns[1]
        for i in range(len(c)):
            if c[i] == "+":
                s += ns[i + 2]
            elif c[i] == "*":
                s *= ns[i + 2]
            else:
                s = s * (10 ** len(str(ns[i + 2]))) + ns[i + 2]
        if s == ns[0]:
            t += ns[0]
            break
print(t)
