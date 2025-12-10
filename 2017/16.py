import re
import sys

import string

sys.path.insert(0, "..")
from util import *


def dance(s: str) -> str:
    for cmd in D.split(","):
        if "s" in cmd:
            x = int(cmd[1:])
            s = s[-x:] + s[:-x]
        elif "x" in cmd:
            a, b = map(int, cmd[1:].split("/"))
            a, b = s[a], s[b]
            s = re.sub(a + "|" + b, lambda m: a if m.group() == b else b, s)
        elif cmd[0] == "p":
            a, b = cmd[1:].split("/")
            s = re.sub(a + "|" + b, lambda m: a if m.group() == b else b, s)
    return s


ans = string.ascii_lowercase[:16]
print(dance(ans))
i = 0
seen = {}
N = 1000000000
while i < N:
    if ans in seen:
        i += (N - i) // (i - seen[ans]) * (i - seen[ans])
    seen[ans] = i
    ans = dance(ans)
    i += 1
print(ans)
