import sys

lines = [l.strip() for l in L]
X = len(lines[0])
Y = len(lines)
ans = 0
x = 0
for y in range(len(lines)):
    if lines[y][x] == "#":
        ans += 1
    x = (x + 3) % X
print(ans)

t = 1
for r, d in [(1, 1), [3, 1], [5, 1], [7, 1], [1, 2]]:
    ans = 0
    x = y = 0
    while y < Y:
        if lines[y][x] == "#":
            ans += 1
        x = (x + r) % X
        y += d
    t *= ans

print(t)
