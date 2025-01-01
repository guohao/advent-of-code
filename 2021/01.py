from util import *

t = 0
for i in range(1, len(I)):
    t += I[i] > I[i - 1]
print(t)

t = 0
for i in range(4, len(I) + 1):
    t += sum(I[i - 3:i]) > sum(I[i - 4:i - 1])
print(t)
