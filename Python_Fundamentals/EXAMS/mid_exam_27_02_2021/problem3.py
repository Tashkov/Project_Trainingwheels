def adding(card_deck: list, card, new_deck: list):
    if card not in card_deck:
        print("Card not found.")
    else:
        new_deck.append(card)

    return new_deck


def inserting(card_deck: list, card, chosen_index: int, new_deck: list):
    if card not in card_deck or not 0 <= chosen_index < len(new_deck):
        print("Error!")
    else:
        new_deck.insert(chosen_index, card)

    return new_deck


def removing(new_deck: list, card):
    if card not in new_deck:
        print("Card not found.")
    else:
        new_deck.remove(card)

    return new_deck


def swap(new_deck: list, first_card, second_card):
    look_through_deck = [card for card in new_deck]
    first_index = look_through_deck.index(first_card)
    second_index = look_through_deck.index(second_card)
    new_deck.remove(first_card)
    new_deck.remove(second_card)
    new_deck.insert(first_index, second_card)
    new_deck.insert(second_index, first_card)

    return new_deck


arsenal_of_cards = input().split(":")
line = input()
battle_deck = []

while not line == "Ready":
    line2 = line.split()
    command = line2[0]
    card_name = line2[1]
    if command == "Add":
        adding(arsenal_of_cards, card_name, battle_deck)
    elif command == "Insert":
        insert_index = int(line2[2])
        inserting(arsenal_of_cards ,card_name, insert_index, battle_deck)
    elif command == "Remove":
        removing(battle_deck, card_name)
    elif command == "Swap":
        second_card_name = line2[2]
        swap(battle_deck, card_name, second_card_name)
    elif command == "Shuffle":
        battle_deck.reverse()

    line = input()

print(*battle_deck, sep=" ")
