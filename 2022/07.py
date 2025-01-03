from util import *

data = D
d = defaultdict(int)
p = []
for line in data.splitlines():
    match line.split():
        case ['$', 'cd', nd]:
            if nd == '..':
                del p[-1]
            else:
                p.append(nd)
        case [size, _] if size.isdigit():
            size = int(size)
            for i in range(len(p)):
                k = '/'.join(p[:i + 1])
                d[k] += size

print(sum(x for x in d.values() if x <= 100000))
require = 30000000 - (70000000 - max(d.values()))
dirs = sorted(d.values())
for i in range(len(dirs)):
    if dirs[i] >= require:
        print(dirs[i])
        break
