import re
import sys
from itertools import product

count_nums = lambda f: sum(map(f, NS))

count_nums = lambda f: sum(map(f, NS))

count_nums = lambda f: sum(map(f, NS))

print(count_nums(lambda x: max(x) - min(x)))

print(
    count_nums(
        lambda ns: sum(
            a // b for a, b in product(ns, repeat=2) if a != b and a % b == 0
        )
    )
)
