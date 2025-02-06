from art import logo, won_logo, lost_logo

import random

print(logo)

def play(attempts, num):
    print(f"You have {attempts} attempts remaining to guess the number. ")
    while attempts > 1:
        guess = int(input("Make a guess: "))
        if guess < num:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number. ")
        elif guess == num:
            print(won_logo)
            print(f"You got it! The answer was {num}.")
            break
        else:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number. ")
    if attempts == 1:
        guess = int(input("Make a guess: "))
        if guess != num:
            attempts -= 1
    # if attempts == 0:
            print(lost_logo)
            print("You\'ve run out of guesses. Refresh the page to run again.")

print("Welcome to the Number Guessing Game!")

print("I\'m thinking of a number between 1 and 100.")
number = random.randint(1,100)

level = input("Choose a difficulty. Type \'easy\' or \'hard\': ")

if level == 'easy':
    number_of_attempts = 10
    play(number_of_attempts, number)
elif level == 'hard':
    number_of_attempts = 5
    play(number_of_attempts, number)
else:
    number_of_attempts = 0

