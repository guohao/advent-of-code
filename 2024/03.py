from util import *

print(sum(math.prod(map(int, m)) for m in re.findall(r'mul\((\d+),(\d+)\)', RAW)))

t = 0
e = True
for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)", RAW):
    if 'don' in m.group():
        e = False
    elif 'do' in m.group():
        e = True
    else:
        if e:
            t += int(m.group(1)) * int(m.group(2))

print(t)
