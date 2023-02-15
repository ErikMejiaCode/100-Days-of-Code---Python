import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# user selection
user_selection = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_selection == 0:
    print(rock)
elif user_selection == 1:
    print(paper)
elif user_selection == 2:
    print(scissors)
else:
    print("You have selected and invalid number")
    exit()


# computer selection
computer_choice = random.randint(0, 2)

print("Computer chose:")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


# winning / losing logic
if (user_selection == 0) and (computer_choice == 0):
    print("Draw.\n")
elif (user_selection == 0) and (computer_choice == 1):
    print("You lose.\n")
elif (user_selection == 0) and (computer_choice == 2):
    print("You Win.\n")
elif (user_selection == 1) and (computer_choice == 0):
    print("You Win.\n")
elif (user_selection == 1) and (computer_choice == 1):
    print("Draw.\n")
elif (user_selection == 1) and (computer_choice == 2):
    print("You lose.\n")
elif (user_selection == 2) and (computer_choice == 0):
    print("You lose.\n")
elif (user_selection == 2) and (computer_choice == 1):
    print("You win.\n")
else:
    print("Draw.\n")
