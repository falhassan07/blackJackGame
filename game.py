import random
from art import logo 


print(logo)


def deal_card():
    """Draws a random card from the deck or list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for card in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(list_of_cards):
    """returns the sum of all the cards in the List as the score"""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

