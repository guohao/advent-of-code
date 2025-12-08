import string
from itertools import product

d = input()
atz = string.ascii_lowercase


def next_c(c):
    return chr((ord(c) - ord("a") + 1) % 26 + ord("a"))


def next_s(s):
    r = s[::-1]
    for i in range(len(r)):
        c = next_c(r[i])
        r = r[:i] + c + r[i + 1 :]
        if c != "a":
            break
    return r[::-1]


def next_pass(p):
    while True:
        p = next_s(p)
        if any(x in p for x in "iol"):
            continue
        if sum(x + x in p for x in atz) < 2:
            continue
        if not any(x + next_c(x) + next_c(next_c(x)) in p for x in atz[:-2]):
            continue
        return p


r1 = next_pass(d)
print(r1)
print(next_pass(r1))
