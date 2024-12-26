from util import *


def parse(s: str) -> str:
    s = s.upper().strip()
    s = s.replace('AND', '&')
    s = s.replace('OR', '|')
    s = s.replace('NOT ', '~')
    s = s.replace('LSHIFT ', '<<')
    s = s.replace('RSHIFT ', '>>')
    return '='.join(reversed(s.split(" -> ")))


def run(b=None):
    q = deque(map(parse, L))
    scope = {}
    while q:
        line = q.popleft()
        if b and line.startswith('B='):
            scope['B'] = b
            continue
        try:
            exec(line, {}, scope)
        except:
            q.append(line)
    return eval('A', scope)


a = run()
print(a)
print(run(a))
