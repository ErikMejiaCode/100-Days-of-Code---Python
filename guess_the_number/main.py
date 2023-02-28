from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """ Checks answer against guess, returns the number of turns remaining """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
# Function to set difficulty 
def set_difficulty():
    """Sets the number of turns in game based on users input"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function initializing the game
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # turns dynamically updated based on set difficulty function
    turns = set_difficulty()

    # repeat functionality if guess is incorrect 
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # letting user guess a number
        guess = int(input("Make a guess: "))
        # tracking the number of turns reduced by 1
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")

game()