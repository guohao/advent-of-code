from util import *

hands = []
cards = 'AKQJT98765432'[::-1]
for line in L:
    hand, bid = line.split()
    points = list(map(cards.index, hand))
    c = Counter(points)
    mc = sorted(c.values())[::-1]
    hands.append(((mc, points), int(bid)))
hands.sort()
print(sum(rnk * bid for rnk, (_, bid) in enumerate(hands, start=1)))

hands = []
cards = 'AKQT98765432J'[::-1]
for line in L:
    hand, bid = line.split()
    points = list(map(cards.index, hand))
    c = Counter(points)
    if 0 < hand.count('J') < 5:
        jc = c.pop(cards.index('J'))
        c[c.most_common()[0][0]] += jc
    mc = sorted(c.values())[::-1]
    hands.append(((mc, points), int(bid)))
hands.sort()
print(sum(rnk * bid for rnk, (_, bid) in enumerate(hands, start=1)))
