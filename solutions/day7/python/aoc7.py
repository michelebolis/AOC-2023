from collections import Counter
lines = [line.strip() for line in open('input.txt').read().split('\n')]

def part1(cards) :
    l2 = ['23456789TJQKA'.index(card) for card in cards]
    occurrencies = tuple(sorted(Counter(cards).values()))
    rank = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2,3), (1,4), (5,)].index(occurrencies)
    return (rank, l2)

def part2(cards):
    l2 = ['J23456789TQKA'.index(card) for card in cards]
    ranks = []
    for key in '23456789TQKA':
        occurrencies = tuple(sorted((Counter(cards.replace('J', key))).values()))
        rank = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2,3), (1,4), (5,)].index(occurrencies)
        ranks.append(rank)
    return (max(ranks), l2)

cards = sorted((part1(cards), int(value)) for cards, value in (line.split() for line in lines))
res = 0
for rank, (_, value) in enumerate(cards): res += rank * value + value
print('Part 1:', res)

cards = sorted((part2(cards), int(value)) for cards, value in (line.split() for line in lines))
res = 0
for rank, (_, value) in enumerate(cards): res += rank * value + value
print('Part 2:', res) 