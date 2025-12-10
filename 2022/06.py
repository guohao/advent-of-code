import sys

import re

data = D


def f(n):
    for i in range(n, len(data)):
        if len(set(data[i - n : i])) == n:
            print(i)
            break


f(4)
f(14)
