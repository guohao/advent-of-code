from util import *

x = 1
s = []
for cmd in L:
    cmd = cmd.strip()
    s.append(x)
    if cmd != 'noop':
        s.append(x)
        x += int(cmd.split()[1])
print(sum(i * s[i - 1] for i in range(20, 260, 40)))
for r in range(6):
    line = ''
    for c in range(40):
        if c in range(s[r * 40 + c] - 1, s[r * 40 + c] + 2):
            line += '#'
        else:
            line += '.'
    print(line)
