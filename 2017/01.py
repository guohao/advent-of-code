import re
import sys

counts = lambda f: sum(map(f, L))

from regex import regex

print(
    counts(
        lambda line: sum(
            map(int, regex.findall(r"(\d)\1", line + line[0], overlapped=True))
        )
    )
)


def f(a):
    r = len(a) // 2
    b = a[-r:] + a[:-r]
    return sum(int(a[i]) for i in range(len(a)) if a[i] == b[i])


print(counts(f))
