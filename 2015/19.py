from util import *

patterns = pairs(lines(PS[0]), "=>")

mm = PS[1].strip()

s = ""
alls = set()
for k, v in patterns:
    alls |= set(
        mm[: patterns.start()] + v + mm[patterns.end() :]
        for patterns in re.finditer(k, mm)
    )
print(len(alls))

r_patterns = [(r[::-1], l[::-1]) for l, r in patterns]
reversed_pattern = "|".join(v for v, _ in r_patterns)
reversed_rules = dict(r_patterns)
rmm = mm[::-1]
count = 0
while rmm != "e":
    rmm = re.sub(
        reversed_pattern, lambda match: reversed_rules[match.group()], rmm, count=1
    )
    count += 1

print(count)
