import regex

from util import *


def f(line):
    ms = [m for m in re.finditer(r'(\w)(\w)\2\1', line) if m.group(1) != m.group(2)]
    if not ms:
        return 0
    if any(line[:m.start()].count('[') - line[:m.start()].count(']') for m in ms):
        return 0
    return 1


def f2(line):
    ins = set()
    outs = set()
    for m in regex.finditer(r'(\w)(\w)\1', line, overlapped=True):
        if m.group(1) == m.group(2):
            continue
        if line[:m.start()].count('[') - line[:m.start()].count(']'):
            ins.add(m.group(1) + m.group(2))
        else:
            outs.add(m.group(2) + m.group(1))
    return len(ins & outs) > 0


print(counts(f))
print(counts(f2))
