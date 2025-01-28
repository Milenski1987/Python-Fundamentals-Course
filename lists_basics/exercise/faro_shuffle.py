cards_deck = input().split()
number_of_shuffles = int(input())
half_deck = len(cards_deck) // 2

for _ in range(number_of_shuffles):
    first_half_deck = cards_deck[:half_deck]
    second_half_deck = cards_deck[half_deck:]
    cards_deck.clear()

    for index in range(half_deck):
        cards_deck.append(first_half_deck[index])
        cards_deck.append(second_half_deck[index])

print(cards_deck)

