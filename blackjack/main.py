import random
import os
from art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_int = random.randint(0, len(cards) - 1)
    random_card = cards[random_int]
    return random_card

def calculate_score(list_of_cards):
    """Takes in a list of cards and return the score calculated from cards"""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0

    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)


def compare(user_score, computer_score):
    """compares the finals scores of users and computer"""
    if user_score == computer_score:
        return "Draw 😅"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 🤯"
    elif user_score == 0:
        return "Win, you have Blackjack 🂡"
    elif user_score > 21:
        return "Lose, bust 🥲"
    elif computer_score > 21:
        return "Win, opponent bust 🥹"
    elif user_score > computer_score:
        return "Win, you have the higher score ♠️"
    else:
        return "Lose, opponent has the higher score ♣️"


def play_game():
    """Main function to inizialize the game"""
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        # calculating scores for both 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Your Cards: {computer_cards[0]}")
        
        # ending game if conditions are met 
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Your final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    cls()
    play_game()
