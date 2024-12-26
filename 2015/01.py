from util import *

print(D.count('(') - D.count(')'))

f = 0
for i, c in enumerate(D, start=1):
    f += 1 if c == '(' else -1
    if f == -1:
        print(i)
        break
