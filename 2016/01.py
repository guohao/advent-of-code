from util import *

ans2 = None
x = y = 0
d = (1, 0)
visited = {(x, y)}
for step in D.split(", "):
    d = turn(d, step[0])
    moves = int(step[1:])
    for i in range(moves):
        x += d[0]
        y += d[1]
        if (x, y) in visited:
            if not ans2:
                ans2 = abs(x) + abs(y)
        visited.add((x, y))
print(abs(x) + abs(y))
print(ans2)
