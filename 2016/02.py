import sys


def move(p, c):
    x, y = p
    match c:
        case "U":
            x -= 1
        case "D":
            x += 1
        case "L":
            y -= 1
        case "R":
            y += 1
    return x, y


def grid(s):
    return {(i, j): c for i, l in enumerate(s.split("\n")) for j, c in enumerate(l)}


def p1():
    x = y = 0
    ans = ""

    for line in L:
        for c in line:
            x, y = move((x, y), c)
            x = max(-1, min(1, x))
            y = max(-1, min(1, y))
        g = {}
        k = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                g[i, j] = k
                k += 1
        ans += str(g[x, y])
    print(ans)


def p2():
    ans = ""
    g = grid("""  1
 234
56789
 ABC
  D""")
    g = {
        (i, j): g[i, j]
        for i in range(5)
        for j in range(5)
        if (i, j) in g and g[i, j].strip()
    }
    x, y = 2, 1
    for line in L:
        for c in line:
            px, py = x, y
            x, y = move((x, y), c)
            if (x, y) not in g:
                x, y = px, py
        ans += g[x, y]
    print(ans)


L = sys.stdin.readlines()
p1()
p2()
