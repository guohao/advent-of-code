import sys

XOR = 'XOR'
AND = 'AND'
OR = 'OR'

g = {}
rg = {}
minmax = lambda _a, _b: (_a, _b) if _a <= _b else (_b, _a)
for line in sys.stdin.read().split('\n\n')[1].splitlines():
    a, op, b, _, c = line.split()
    a, b = minmax(a, b)
    g[a, b, op] = c
    rg[c] = a, b, op


def swap(_a, _b):
    rg[_a], rg[_b] = rg[_b], rg[_a]
    g[rg[_a]], g[rg[_b]] = g[rg[_b]], g[rg[_a]]


output = set()
c = ''
for i in range(int(max(rg)[1:])):
    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'
    zn = f'z{i + 1:02}'
    xxy = g[x, y, XOR]
    xay = g[x, y, AND]
    if not c:
        c = xay
    else:
        a, b = minmax(c, xxy)
        k = a, b, XOR
        if k not in g:
            a, b = list(set(rg[z][:2]) ^ set(k[:2]))
            output.add(a)
            output.add(b)
            swap(a, b)
        elif g[k] != z:
            output.add(g[k])
            output.add(z)
            swap(z, g[k])
        k = rg[z]
        xxy = g[x, y, XOR]
        xay = g[x, y, AND]
        c = g[*minmax(c, xxy), AND]
        c = g[*minmax(c, xay), OR]

print(','.join(sorted(output)))
