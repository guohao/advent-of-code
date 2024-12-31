from util import *

mapper = {}

image = '.#./..#/###'


def rotate(g, times):
    for _ in range(times):
        g = [list(x[::-1]) for x in zip(*g)]
    return g


def flip(g):
    return g[::-1]


def rotate_flip(g):
    rfs = []
    for i in range(4):
        rfs.append(rotate(g, i))
    for r in rfs.copy():
        rfs.append(flip(r))
    for r in rfs.copy():
        rfs.append([x[::-1] for x in r])
    return set('/'.join(''.join(line) for line in rf) for rf in rfs)


def parse_input(lines):
    for line in lines:
        f, t = map(str.strip, line.split('=>'))
        for x in rotate_flip([list(x) for x in f.split('/')]):
            mapper[x] = t


def map_image(origin):
    lines = origin.split('/')
    n = len(lines)
    if n % 2 == 0:
        new = [''] * (n // 2 * 3)
        for i, j in product(range(0, n, 2), repeat=2):
            mapped = mapper['/'.join(''.join(lines[i + q][j + p] for p in range(2)) for q in range(2))]
            parts = mapped.split('/')
            for k in range(3):
                new[i // 2 * 3 + k] += parts[k]
    else:
        new = [''] * (n // 3 * 4)
        for i, j in product(range(0, n, 3), repeat=2):
            mapped = mapper['/'.join(''.join(lines[i + q][j + p] for p in range(3)) for q in range(3))]
            parts = mapped.split('/')
            for k in range(4):
                new[i // 3 * 4 + k] += parts[k]
    return '/'.join(new)


parse_input(L)

for _ in range(5):
    image = map_image(image)
print(image.count('#'))

for _ in range(13):
    image = map_image(image)
print(image.count('#'))
