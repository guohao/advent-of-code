import sys

d = input().strip()


def count_say(s):
    s = s + "-"
    r = ""
    j = 1
    prev = s[0]
    for i, c in enumerate(s[1:]):
        if c == prev:
            j += 1
        else:
            r += str(j) + prev
            j = 1
            prev = c
    return r


def run(times):
    cs = d
    for i in range(times):
        cs = count_say(cs)
    print(len(cs))


run(40)
run(50)
