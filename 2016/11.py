from util import *


def tuple_state(_state: list[tuple]):
    ret = []
    idx = {e: i for i, fl in enumerate(_state) for e in fl}
    for fl in _state:
        pair = set(a for a in fl if any(b[0] == a[0] for b in fl if a != b))
        single = set(fl) - pair
        ms = set(a for a in single if a[-1] == 'M')
        gs = set(a for a in single if a[-1] == 'G')
        msg = frozenset(idx[m[0] + 'G'] for m in ms)
        gsm = frozenset(idx[g[0] + 'M'] for g in gs)
        ret.append((len(pair) // 2, len(ms), len(gs), msg, gsm))
    return tuple(ret)


def f(l: list[str]):
    height = len(l)
    init_state = []
    for line in l:
        cur_fl = []
        for mg in re.findall(r'\S+ microchip|\S+ generator', line):
            n, t = mg.split()
            cur_fl.append(f'{n[0].upper()}{t[0].upper()}')
        init_state.append(tuple(sorted(cur_fl)))
    hp = [(0, 0, *init_state)]
    seen = set()
    while hp:
        step, cur_fl, *state = heapq.heappop(hp)
        k = (cur_fl, tuple_state(state))
        if k in seen:
            continue
        seen.add(k)
        if sum(map(len, state[:-1])) == 0:
            print(step)
            break
        for fl in state:
            ms = set(m[0] for m in fl if m[1] == 'M')
            gs = set(g[0] for g in fl if g[1] == 'G')
            if gs and any(x not in gs for x in ms):
                break
        else:
            for next_fl in {cur_fl + 1, cur_fl - 1} & set(range(height)):
                for c in chain(combinations(state[cur_fl], 1), combinations(state[cur_fl], 2)):
                    next_state = list(state)
                    next_state[cur_fl] = tuple(e for e in state[cur_fl] if e not in c)
                    next_state[next_fl] = tuple(sorted(state[next_fl] + c))
                    heapq.heappush(hp, (step + 1, next_fl, *next_state))


f(L)
L[0] += ' elerium generator elerium-compatible microchip dilithium generator dilithium-compatible microchip'
f(L)
