import sys

import re

t = 0
for line in L:
    l, r = line.split("|")
    i, p = l.split(":")
    ps = set(map(int, p.split()))
    t += round(2 ** (len(set(map(int, r.split())) & ps) - 1))

print(t)

pows = [1] * R
for i, line in enumerate(L):
    l, r = line.split("|")
    _, p = l.split(":")
    n = len(set(map(int, r.split())) & set(map(int, p.split())))
    for j in range(i + 1, i + 1 + n):
        pows[j] += pows[i]

print(sum(pows))
