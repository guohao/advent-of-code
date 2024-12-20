import sys
from collections import deque

data = sys.stdin.read().strip()

qs = []
for part in data.split('\n\n'):
    qs.append(deque(map(int, part.splitlines()[1:])))


def game(cqs):
    seen = [set() for _ in range(2)]
    while all(cqs):
        if any(tuple(cqs[i]) in seen[i] for i in range(2)):
            return 0
        for i in range(2):
            seen[i].add(tuple(cqs[i]))
        if all(cqs[i][0] < len(cqs[i]) for i in range(2)):
            nqs = [deque(list(q)[1:1 + q[0]]) for q in cqs]
            win_idx = game(nqs)
        else:
            win_idx = int(cqs[1][0] > cqs[0][0])
        cqs[win_idx].append(cqs[win_idx].popleft())
        cqs[win_idx].append(cqs[1 - win_idx].popleft())
    return int(not cqs[0])


w = qs[game(qs)]
print(sum(w.popleft() * i for i in range(len(w), 0, -1)))
