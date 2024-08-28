import random
from art import logo 


print(logo)


def deal_card():
    """Draws a random card from the deck or list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

