d = input()


def move(ins):
    g = {(0, 0)}
    i = j = 0
    for c in ins:
        match c:
            case "<":
                j -= 1
            case ">":
                j += 1
            case "v":
                i += 1
            case "^":
                i -= 1
        g.add((i, j))
    return g


print(len(move(d)))
print(len(move(d[::2]) | move(d[1::2])))
