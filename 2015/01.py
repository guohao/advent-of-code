from util import *

d = raw()
print(d.count('(') - d.count(')'))

f = 0
for i, c in enumerate(d, start=1):
    f += 1 if c == '(' else -1
    if f == -1:
        print(i)
        break
