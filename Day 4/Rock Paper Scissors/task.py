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

options = [rock, paper, scissors]
options_string = ['Rock', 'Paper', 'Scissors']

user_choice = int(input(f"Enter your choice: 0 for rock, 1 for paper, 2 for scissors? "))

if user_choice in [0,1,2]:
    print(f"The user chose: {options_string[user_choice]}")
    print(options[user_choice])
else:
    print(f"Please choose a valid option.")

computer_choice = random.randint(0,2)
print(f"The computer chose {options_string[computer_choice]}.")
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and options[computer_choice] == scissors:
    print("You won!")
elif user_choice == 1 and options[computer_choice] == rock:
    print("You won!")
elif user_choice == 2 and options[computer_choice] == paper:
    print("You won!")
else:
    print("Sorry you lost!")
