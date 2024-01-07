with open ("inputday7.txt") as f:
    lines = f.read().split('\n')

#Map the cards in order of the alphabet
letter_map = {"T": "A", "J":"B", "Q":"C", "K":"D", "A":"E"}    

#counts contains how many times each card is in the hand
#e.g.: AAA3T -> [3,3,3,1,1]
def classify(hand):
    counts = [hand.count(card) for card in hand]
    #5 of a kind
    if 5 in counts:
        return 6
    #4 of a kind
    if 4 in counts:
        return 5
    if 3 in counts:
        #full house
        if 2 in counts:
            return 4
        #3 of a kind
        return 3
    #2 pairs
    if counts.count(2) == 4:
        return 2
    #1 pair
    if 2 in counts:
        return 1
    #all different
    return 0

#returns a tuple containing the (value of the hand, a list with mapped letters of the hand)
def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])    

plays = []
for line in lines:
    hand, bid = line.split()
    plays.append((hand, int(bid)))

#sorts by hand value, then by card value
plays.sort(key = lambda x: strength(x[0]))

total = 0
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)