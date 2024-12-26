from util import *
import string
import re


def f(s: str) -> bool:
    return (
            sum(s.count(x) for x in 'aeiou') >= 3 and
            any(x * 2 in s for x in string.ascii_lowercase) and
            not any(x in s for x in ['ab', 'cd', 'pq', 'xy'])
    )


f2 = lambda s: bool(re.search(r'(\w{2}).*\1', s) and re.search(r'(\w)\w\1', s))

print(counts(f))
print(counts(f2))
