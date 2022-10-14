deck_of_cards = input().split()
number_shuffels = int(input())
counter = 0

while counter != number_shuffels:
    middle_of_deck = len(deck_of_cards) // 2

    deck_a = deck_of_cards[:middle_of_deck:]
    deck_b = deck_of_cards[middle_of_deck::]

    shuffelled_deck = []

    for number in range(len(deck_a)):
        shuffelled_deck.append(deck_a[number])
        shuffelled_deck.append(deck_b[number])
    deck_of_cards = shuffelled_deck.copy()

    counter += 1
print(deck_of_cards)