import re
import sys


def move(p, d):
    _arrow_dirs = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    LDRU_DIRS = {"L": (0, -1), "D": (1, 0), "R": (0, 1), "U": (-1, 0)}
    if d in _arrow_dirs:
        return tuple_add(p, _arrow_dirs[d])
    elif d in LDRU_DIRS:
        return tuple_add(p, LDRU_DIRS[d])


def tuple_add(_a, _b) -> tuple[int, ...]:
    """Adds two tuples of the same length"""
    assert len(_a) == len(_b)
    return tuple(_a[i] + _b[i] for i in range(len(_a)))


_arrow_dirs = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
LDRU_DIRS = {"L": (0, -1), "D": (1, 0), "R": (0, 1), "U": (-1, 0)}


def move(p, d):
    if d in _arrow_dirs:
        return tuple_add(p, _arrow_dirs[d])
    elif d in LDRU_DIRS:
        return tuple_add(p, LDRU_DIRS[d])


RAW = sys.stdin.read()


def p1():
    maze, path = RAW.split("\n\n")
    if maze[0] == "\n":
        maze = maze[1:]
    path = "R" + path

    g = {
        (i, j): c
        for i, line in enumerate(maze.splitlines())
        for j, c in enumerate(line)
        if c != " "
    }
    limits = (
        min(x for x, _ in g),
        max(x for x, _ in g),
        min(y for _, y in g),
        max(y for _, y in g),
    )
    N = limits[1] - limits[0] + 1
    M = limits[3] - limits[2] + 1

    def neighbor(p, facing) -> (int, int):
        assert p
        limit = N if facing[0] != 0 else M
        for _ in range(limit):
            np = ((p[0] + facing[0]) % N, (p[1] + facing[1]) % M)
            if np in g:
                if g[np] == ".":
                    return np
                elif g[np] == "#":
                    return None
            p = np

    p = (0, maze.index("."))
    facing = (-1, 0)
    for move in re.findall(r"[RL]\d+", path):
        steps = int(move[1:])
        direction = move[0]
        if direction == "R":
            facing = (facing[1], -facing[0])
        else:
            facing = (-facing[1], facing[0])
        for i in range(steps):
            np = neighbor(p, facing)
            if np:
                p = np
            else:
                break

    ans = 1000 * (p[0] + 1) + 4 * (p[1] + 1)
    match facing:
        case (0, 1):
            ans += 0
        case (1, 0):
            ans += 1
        case (0, -1):
            ans += 2
        case (-1, 0):
            ans += 3
    print(ans)


def p2():
    maze, path = RAW.split("\n\n")
    if maze[0] == "\n":
        maze = maze[1:]
    path = "R" + path

    g = {
        (i, j): c
        for i, line in enumerate(maze.splitlines())
        for j, c in enumerate(line)
        if c != " "
    }

    neighbors = {}

    def neighbor(p, facing) -> ((int, int), (int, int)):
        np = ((p[0] + facing[0]), (p[1] + facing[1]))
        if np not in g:
            np, facing = neighbors[p, facing]
        if g[np] != "#":
            return np, facing
        return None, None

    """
      .AB
      .C.
      ED.
      F..
      """
    p = (0, maze.index("."))
    facing = (-1, 0)
    K = 50
    for i in range(0, K):
        # A -> F
        neighbors[(0, K + i), (-1, 0)] = ((3 * K + i, 0), (0, 1))
        # A -> E
        neighbors[(i, K), (0, -1)] = ((3 * K - 1 - i, 0), (0, 1))
        # B -> C
        neighbors[(K - 1, 2 * K + i), (1, 0)] = ((K + i, 2 * K - 1), (0, -1))
        # B -> F
        neighbors[(0, 2 * K + i), (-1, 0)] = (4 * K - 1, i), (-1, 0)
        # B -> D
        neighbors[(i, 3 * K - 1), (0, 1)] = ((3 * K - 1 - i, 2 * K - 1), (0, -1))
        # C -> E
        neighbors[(K + i, K), (0, -1)] = ((2 * K, i), (1, 0))
        # C -> B
        neighbors[(K + i, 2 * K - 1), (0, 1)] = ((K - 1, 2 * K + i), (-1, 0))
        # D -> B
        neighbors[(2 * K + i, 2 * K - 1), (0, 1)] = ((K - 1 - i, 3 * K - 1), (0, -1))
        # D -> F
        neighbors[(3 * K - 1, K + i), (1, 0)] = ((3 * K + i, K - 1), (0, -1))
        # E -> A
        neighbors[(2 * K + i, 0), (0, -1)] = ((K - 1 - i, K), (0, 1))
        # E -> C
        neighbors[(2 * K, i), (-1, 0)] = ((K + i, K), (0, 1))
        # F -> A
        neighbors[(3 * K + i, 0), (0, -1)] = ((0, K + i), (1, 0))
        # F -> B
        neighbors[(4 * K - 1, i), (1, 0)] = ((0, 2 * K + i), (1, 0))
        # F -> D
        neighbors[(3 * K + i, K - 1), (0, 1)] = ((3 * K - 1, K + i), (-1, 0))

    for move in re.findall(r"[RL]\d+", path):
        steps = int(move[1:])
        direction = move[0]
        if direction == "R":
            facing = (facing[1], -facing[0])
        else:
            facing = (-facing[1], facing[0])
        for i in range(steps):
            np, nf = neighbor(p, facing)
            if np:
                p = np
                facing = nf

    ans = 1000 * (p[0] + 1) + 4 * (p[1] + 1)
    match facing:
        case (0, 1):
            ans += 0
        case (1, 0):
            ans += 1
        case (0, -1):
            ans += 2
        case (-1, 0):
            ans += 3
    print(ans)


p1()
p2()
