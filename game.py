import random
from art import logo 


def deal_card():
    """Draws a random card from the deck or list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    """returns the sum of all the cards in the List as the score"""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw.🙃"
    elif c_score == 0:
        return "You Lose. Computer has blackjack. 😱"
    elif u_score == 0:
        return "You win with a blackjack. 😎"
    elif u_score > 21:
        return "You went over. You lose. 😭"
    elif c_score > 21:
        return "Computer went over. You win. 😁"
    elif u_score > c_score:
        return "You win. 😄"
    else:
        return "You lose. 😒"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for card in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack. 'y' for yes or 'n' for 'no': ").lower() == "y":
    print("\n"*20)
    play_game()

