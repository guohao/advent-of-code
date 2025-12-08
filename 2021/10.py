from util import *

t = 0
q = deque()
pairs = {"{": "}", "(": ")", "<": ">", "[": "]"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
lines = [l.strip() for l in L]

for line in lines:
    for c in line:
        if c in "[{<(":
            q.append(c)
        else:
            if pairs[q[-1]] != c:
                t += points[c]
                break
            else:
                q.pop()
print(t)


def score_of(line: str):
    q = deque()
    pairs = {"{": "}", "(": ")", "<": ">", "[": "]"}
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    for c in line:
        if c in "[{<(":
            q.append(c)
        else:
            if pairs[q[-1]] != c:
                return 0
            else:
                q.pop()
    score = 0
    while q:
        score = score * 5 + points[q.pop()]
    return score


seq = sorted(list(filter(lambda x: x > 0, map(score_of, lines))))
print(seq[len(seq) // 2])
