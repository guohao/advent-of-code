import sys

ls = sys.stdin.readlines()


def run(part2, b):
    ws = {}
    cmds = []
    for l in ls:
        left, right = l.strip().split("->")[::-1]
        if left.strip() == "b" and part2:
            ws["B"] = b
            continue
        right = "(" + right + ")&0xffff"
        l = left + "=" + right
        l = l.strip().upper()
        l = l.replace("AND", "&")
        l = l.replace("OR", "|")
        l = l.replace("LSHIFT", "<<")
        l = l.replace("RSHIFT", ">>")
        l = l.replace("NOT", "~")
        cmds.append(l)
    while cmds:
        nc = []
        for c in cmds:
            try:
                exec(c, ws)
            except Exception as e:
                nc.append(c)
                pass
        cmds = nc
    return ws["A"]


a = run(False, -1)
print(a)
print(run(True, a))
