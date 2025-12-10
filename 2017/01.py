d = input().strip()
print(sum(int(d[i]) for i in range(len(d)) if d[i] == d[(i + 1) % len(d)]))

r = len(d) // 2
print(sum(int(d[i]) for i in range(len(d)) if d[i] == d[(i + r) % len(d)]))
