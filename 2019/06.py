import sys
from collections import deque, defaultdict

L = sys.stdin.readlines()
G = defaultdict(list)
for line in L:
    a, b = line.strip().split(")")
    G[a].append(b)


def count_descendants(node):
    total = len(G[node])
    for child in G[node]:
        total += count_descendants(child)
    return total


print(sum(count_descendants(n) for n in list(G.keys())))

G_undirected = defaultdict(list)
for line in L:
    a, b = line.strip().split(")")
    G_undirected[a].append(b)
    G_undirected[b].append(a)


def bfs_shortest_path(start, end):
    if start not in G_undirected or end not in G_undirected:
        return None
    q = deque([(start, 0)])
    visited = {start}
    while q:
        node, dist = q.popleft()
        if node == end:
            return dist
        for neighbor in G_undirected[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
    return None


result = bfs_shortest_path("YOU", "SAN")
if result is not None:
    print(result - 2)
else:
    print(0)
