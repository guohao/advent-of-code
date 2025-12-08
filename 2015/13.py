from util import *

d = defaultdict(int)
p = set()
for line in L:
    a, c, v, b = re.search(r"(\w+).*(gain|lose) (\d+).* (\w+)", line).groups()
    v = int(v)
    p.add(a)
    d[a, b] = v if c == "gain" else -v


def total_change(persons):
    return max(
        sum(d[k[::-1]] + d[k] for k in zip(c, c[1:] + (c[0],)))
        for c in permutations(persons)
    )


print(total_change(p))
print(total_change(p | {"me"}))
