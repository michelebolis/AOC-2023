games = list(open("input.txt"))
part1 = 0
cardCopies = [1 for _ in games]

for cardIndex, game in enumerate(games):
    gamePoint = 0
    deck = [part for part in game.split(": ")][1].strip().split(" | ")
    winningcards = [int(card) for card in deck[0].split(" ") if card.isnumeric()]
    mycard = [int(card) for card in deck[1].split(" ") if card.isnumeric()]

    gamePoint = len(set(winningcards) & set(mycard)) # assuntion: no duplicate cards
    if gamePoint>0 :
        part1 += 2**(gamePoint-1)
        for i in range(gamePoint): cardCopies[i + cardIndex + 1] += cardCopies[cardIndex]

print("Part 1:", part1)
print("Part 2:", sum(cardCopies))