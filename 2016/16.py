import re
import sys

D = input().strip()


def f(n):
    d = D
    while len(d) < n:
        d = d + "0" + re.sub(r"\d", lambda m: str(1 - int(m.group())), d[::-1])
    d = d[:n]
    while True:
        d = re.sub(r"(\d)(\d)", lambda m: str(int(m.group(1) == m.group(2))), d)
        if len(d) % 2:
            print(d)
            break


f(272)
f(35651584)
