import sys
import re

a, b = sys.stdin.read().split("\n\n")
b = b.strip()
ms = set()
r_patterns = []
for l in a.split("\n"):
    f, t = map(str.strip, l.strip().split("=>"))
    r_patterns.append((t[::-1], f[::-1]))
    for m in re.finditer(f, b):
        ms.add(b[: m.start()] + t + b[m.end() :])
print(len(ms))

reversed_pattern = "|".join(v for v, _ in r_patterns)
reversed_rules = dict(r_patterns)
rb = b[::-1]
count = 0
while rb != "e":
    rb = re.sub(
        reversed_pattern, lambda match: reversed_rules[match.group()], rb, count=1
    )
    count += 1

print(count)
