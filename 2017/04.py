from util import *

print(counts(lambda line: len(line.split()) == len(set(line.split()))))


def f(line):
    a = [''.join(sorted(x)) for x in line.split()]
    return len(a) == len(set(a))


print(counts(f))
