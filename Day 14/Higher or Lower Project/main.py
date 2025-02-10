# Perform necessary imports
from art import logo, vs
from game_data import data
import random


def extract_data(lst):
    """Extract_data function takes in a list as input and returns data from the list in a particular format"""
    name = lst["name"]
    follower_count = lst["follower_count"]
    description = lst["description"]
    country = lst["country"]
    return f"{name}, {description}, from {country}", follower_count


def highest_followers(lst1, lst2):
    """Highest_followers function takes in 2 lists as inputs, extracts the follower_count from each list and returns the name of the string with the highest follower_count"""
    lst1_data = extract_data(lst1)
    follower_count1 = lst1_data[1]
    lst2_data = extract_data(lst2)
    follower_count2 = lst2_data[1]
    if follower_count1 > follower_count2:
        return "a"
    else:
        return "b"

# main

print(logo)
game_score = 0

should_continue = True      # Decides if the game should continue or not

b = random.choice(data)     # A random dictionary is chosen from data list defined in game_data.py

# Below loop continues till the user is correct
while should_continue:

    a = b                   # Making data at position B become the next data at position A.
    b = random.choice(data) # Choosing new data at position B

    # Converting data
    a_data = extract_data(a)
    b_data = extract_data(b)

    # Displaying the game
    # print(logo)

    print(f"Compare A: {a_data[0]}")

    print(vs)

    print(f"Against B: {b_data[0]}")

    # User makes a guess
    user_guess = input(f"Who has more followers? Type \'A\' or \'B\': ").lower()

    # Clears the screen
    print("\n" * 20)
    print(logo)

    # Checks if the user is correct at the guess or not
    if user_guess == highest_followers(a,b):    # The user is correct, game continues
        game_score += 1
        should_continue = True
        print(f"You\'re right! Current score: {game_score}.")
    else:   # The user is wrong, game ends
        print(f"Sorry, that\'s wrong. Final Score: {game_score}.")
        should_continue = False
        break

    # Game ends






# Previous code -
# a_list = random.choice(data)
# a_list_name = a_list["name"]
# a_list_followers = a_list["follower_count"]
# a_list_description = a_list["description"]
# a_list_country = a_list["country"]
# print(f"Compare A: {a_list_name}, {a_list_description}, from {a_list_country}.")
#
# print(vs)
#
# b_list = random.choice(data)
# b_list_name = b_list["name"]
# b_list_followers = b_list["follower_count"]
# b_list_description = b_list["description"]
# b_list_country = b_list["country"]
# print(f"Against B: {b_list_name}, {b_list_description}, from {b_list_country}.")
#
# user_guess = input(f"Who has more followers? Type \'A\' or \'B\': ")
# game_score = 0
#
# if user_guess == highest_followers(a_list_followers, b_list_followers):
#
#     game_score += 1
#     print(f"You\'re right! Current score = {game_score}.")
# else:
#     print(user_guess)
#     print(highest_followers(a_list_followers, b_list_followers))
#     print(f"Sorry, that\'s wrong. Final Score: {game_score}.")


