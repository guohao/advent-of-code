from itertools import permutations
import sys

import re


def join(l):
    return "".join(map(str, l))


print(
    len(
        list(
            p
            for line in L
            for p in line.strip().split("|")[1].split()
            if len(p) in (2, 3, 4, 7)
        )
    )
)

t = 0
d = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}
for line in L:
    l, r = line.split("|")
    atg = "abcdefg"
    for perm in permutations(atg):
        m = {perm[i]: atg[i] for i in range(len(atg))}

        def normalize(s):
            return "".join(sorted(m[c] for c in s))

        if all(normalize(x) in d for x in l.split()):
            t += int("".join(d[normalize(x)] for x in r.split()))
            break
print(t)
