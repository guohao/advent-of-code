from util import *
d = list(map(int, D.split()))

t = 0
i = 0


def dfs():
    global t
    global i
    cc = d[i]
    mc = d[i + 1]
    i += 2
    for _ in range(cc):
        dfs()
    t += sum(d[i:i + mc])
    i += mc


dfs()
print(t)

i = 0
def dfs() -> int:
    t = 0
    global i
    cc = d[i]
    mc = d[i + 1]
    i += 2
    children = [dfs() for _ in range(cc)]
    metadata = d[i:i + mc]
    c = Counter(metadata)
    if not cc:
        t += sum(metadata)
    else:
        t += sum(children[j] * c[j + 1] for j in range(cc) if (j + 1))
    i += mc
    return t


print(dfs())
