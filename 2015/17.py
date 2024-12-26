from util import *


def s():
    for i in range(R):
        ss = sum(sum(p) == 150 for p in combinations(I, i))
        if ss:
            yield ss


print(sum(s()))
print(next(s()))
