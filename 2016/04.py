import sys
import re
from collections import Counter


def f(line):
    name, i, cs = re.findall(r"(\w.*)-(\d+)\[(\w+)]", line)[0]
    if cs == "".join(
        x[0] for x in Counter(sorted(name.replace("-", ""))).most_common(5)
    ):
        return int(i)
    return 0


ls = sys.stdin.readlines()

print(sum(map(f, ls)))

for line in ls:
    name, sid, _ = re.findall(r"(\w.*)-(\d+)\[(\w+)]", line)[0]
    decode = "".join(
        chr(ord("a") + (ord(c) - ord("a") + int(sid)) % 26)
        for c in name.replace("-", "")
    )
    if "NorthPoleobjects".lower() in decode:
        print(sid)
        break
