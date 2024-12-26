from util import *


def f(line):
    name, i, cs = re.findall(r'(\w.*)-(\d+)\[(\w+)]', line)[0]
    if cs == ''.join(x[0] for x in Counter(sorted(name.replace('-', ''))).most_common(5)):
        return int(i)
    return 0


print(counts(f))

for line in L:
    name, sid, _ = re.findall(r'(\w.*)-(\d+)\[(\w+)]', line)[0]
    decode = join(chr(ord('a') + (ord(c) - ord('a') + int(sid)) % 26) for c in name.replace("-", ''))
    if 'NorthPoleobjects'.lower() in decode:
        print(sid)
        break
