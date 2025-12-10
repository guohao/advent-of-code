from collections import Counter
from itertools import product
import sys

import re


def join(l):
    return "".join(map(str, l))


N = 150
print(
    min(
        [
            (c["0"], c["1"] * c["2"])
            for c in [Counter(D[i : i + N]) for i in range(0, len(D), N)]
        ]
    )[1]
)

output = ["2"] * N
for i, j in product(range(0, len(D), N), range(N)):
    if output[j] == "2":
        output[j] = D[i + j]

for i in range(6):
    line = "".join(
        map(lambda x: " " if x == "0" else "#", output[i * 25 : (i + 1) * 25])
    )
    print(line)
