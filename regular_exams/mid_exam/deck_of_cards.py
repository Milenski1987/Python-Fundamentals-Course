def add(deck_of_cards: list[str], name_of_card: str) -> list[str]:
    if name_of_card in deck_of_cards:
        print("Card is already in the deck")
        return deck_of_cards
    deck_of_cards.append(name_of_card)
    print("Card successfully added")
    return deck_of_cards


def remove(deck_of_cards: list[str], name_of_card: str) -> list[str]:
    if name_of_card in deck_of_cards:
        deck_of_cards.remove(name_of_card)
        print("Card successfully removed")
        return deck_of_cards
    print("Card not found")
    return deck_of_cards


def remove_at(deck_of_cards: list[str], index_of_card: int) -> list[str]:
    if index_of_card not in range(len(deck_of_cards)):
        print("Index out of range")
        return deck_of_cards
    deck_of_cards.pop(index_of_card)
    print("Card successfully removed")
    return deck_of_cards


def insert(deck_of_cards: list[str], index_of_card: int, name_of_card: str) -> list[str]:
    if index_of_card not in range(len(deck_of_cards)):
        print("Index out of range")
        return deck_of_cards
    if name_of_card in deck_of_cards:
        print("Card is already added")
        return deck_of_cards
    deck_of_cards.insert(index_of_card, name_of_card)
    print("Card successfully added")
    return deck_of_cards


def main():
    initial_deck_of_cards = input().split(", ")
    number_of_commands = int(input())

    for _ in range(number_of_commands):
        command = input()
        action = command.split(", ")[0]

        if action == "Add":
            card_name = command.split(", ")[1]
            initial_deck_of_cards = add(initial_deck_of_cards, card_name)
        elif action == "Remove":
            card_name = command.split(", ")[1]
            initial_deck_of_cards = remove(initial_deck_of_cards, card_name)
        elif action == "Remove At":
            card_index = int(command.split(", ")[1])
            initial_deck_of_cards = remove_at(initial_deck_of_cards, card_index)
        elif action == "Insert":
            card_index = int(command.split(", ")[1])
            card_name = command.split(", ")[2]
            initial_deck_of_cards = insert(initial_deck_of_cards, card_index, card_name)

    print(", ".join(initial_deck_of_cards))


main()