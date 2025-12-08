from util import *

seeds = list(map(int, PS[0].split(":")[1].split()))
parts = [part.splitlines()[1:] for part in PS[1:]]
ans = []
for s in seeds:
    for mappings in parts:
        for m in mappings:
            ts, fs, rl = map(int, m.split())
            if fs <= s < fs + rl:
                s = ts + s - fs
                break
    else:
        ans.append(s)

print(sorted(ans)[0])

seeds = deque([(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)])
for mappings in parts:
    ns = deque()
    while seeds:
        ss, srl = seeds.popleft()
        for m in mappings:
            ts, fs, mrl = map(int, m.split())
            if fs <= ss < fs + mrl:
                ns.append((ts + ss - fs, min(ss + srl, fs + mrl) - ss))
                if ss + srl > fs + mrl:
                    seeds.append((fs + mrl, ss + srl - fs - mrl))
                break
    seeds = ns

print(sorted(seeds)[0][0])
