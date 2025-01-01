from util import *
from regex import regex


def f0(line):
    ns = list(map(int, re.findall(r'\d', line)))
    return ns[0] * 10 + ns[-1]


print(counts(f0))


def f(line):
    ws = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    d2i = lambda x: ws.index(x) if x in ws else int(x)
    ns = list(map(d2i, regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)))
    return ns[0] * 10 + ns[-1]


print(counts(f))
