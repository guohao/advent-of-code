import sys

import re

sys.path.insert(0, "..")
from util import *

data = D

cards = list(range(10007))
for line in data.splitlines():
    if "new stack" in line:
        cards.reverse()
    elif "cut" in line:
        n = int(line.split()[-1])
        cards = cards[n:] + cards[:n]
    else:
        n = int(line.split()[-1])
        n_cards = [0 for _ in range(len(cards))]
        i = 0
        for c in cards:
            n_cards[i] = c
            i = (i + n) % len(n_cards)
        cards = n_cards
print(cards.index(2019))

data = D

nc, times = 119315717514047, 101741582076661

add, mul = 0, 1
for line in data.splitlines():
    if "new stack" in line:
        mul *= -1
        add += mul
    elif "cut" in line:
        n = int(line.split()[-1])
        add += n * mul
    else:
        n = int(line.split()[-1])
        mul *= pow(n, -1, nc)

mul_inv = pow(1 - mul, -1, nc)
muls = pow(mul, times, nc)
adds = add * (1 - muls) * mul_inv

print((2020 * muls + adds) % nc)
