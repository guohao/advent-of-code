import sys

I = [int(line.strip()) for line in sys.stdin.readlines()]
t = 0
for i in range(1, len(I)):
    t += I[i] > I[i - 1]
print(t)

t = 0
for i in range(3, len(I)):
    t += I[i] > I[i - 3]
print(t)
