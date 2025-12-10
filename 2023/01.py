import re
import sys

L = sys.stdin.readlines()


def f0(line):
    ns = list(map(int, re.findall(r"\d", line)))
    return ns[0] * 10 + ns[-1]


print(sum(f0(line) for line in L))


def f(line):
    ws = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    d2i = lambda x: ws.index(x) if x in ws else int(x)
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    ns = [d2i(m.group(1)) for m in re.finditer(pattern, line)]
    return ns[0] * 10 + ns[-1]


print(sum(f(line) for line in L))
