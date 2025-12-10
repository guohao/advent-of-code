import re
import sys


def ext(ints):
    if all(x == 0 for x in ints):
        return 0
    return ints[-1] + ext([ints[i] - ints[i - 1] for i in range(1, len(ints))])


print(sum(map(ext, NS)))


def ext2(ns):
    if all(x == 0 for x in ns):
        return 0
    return ns[0] - ext2([ns[i] - ns[i - 1] for i in range(1, len(ns))])


print(sum(map(ext2, NS)))
