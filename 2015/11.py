import string

from util import *

lts = string.ascii_lowercase


def increase(s: str):
    for i in range(len(s) - 1, -1, -1):
        idx = lts.index(s[i])
        if idx != 25:
            return s[:i] + lts[idx + 1] + ('a' * (len(s) - i - 1))


increasings = set(lts[i] + lts[i + 1] + lts[i + 2] for i in range(24))
pairs = set(c + c for c in lts)


def f(s):
    while True:
        s = increase(s)
        if any(c in s for c in 'iol'):
            continue
        if not any(c in s for c in increasings):
            continue
        if sum(p in s for p in pairs) < 2:
            continue
        return s


print(f(D))
print(f(f(D)))
