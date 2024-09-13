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

print("Welcome to the Rock Paper Scissors game!\n")
print("The basic rules are:")
print("1.Rock wins against scissors.\n2.Scissors win against paper.\n3.Paper wins against rock.\n")

def get_user_choice():
    while True:
        choice = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

user_choice = get_user_choice()
computer_choice = random.randint(1, 3)
options = [rock, paper, scissors]

print(f"Your choice: {user_choice}")
print(options[user_choice - 1])
print(f"Computer choice: {computer_choice}")
print(options[computer_choice - 1])

if user_choice == computer_choice:
    print("It's a draw, there are no winners.")
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 3 and computer_choice == 2):
    print("You WON!")
else:
    print("You lost!")