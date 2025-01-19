import art
import random


def deal_card():
    global cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_score(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose 😭"

    elif computer_score > 21:
        return "Opponent went over. You win 😁"

    elif user_score == 0:
        return "Win with a Blackjack 😎"

    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"

    if user_score > computer_score:
        return "You win 😃"


    elif user_score == computer_score:
        return "Draw 🙃"

    else:
        return "You lose 😤"


def play_game():
    # print(art.logo)

    while True:
        play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")
        if play == 'y':
            print("\n" * 20)
            print(art.logo)

            game_over = False

            user_cards = []
            computer_cards = []
            #user_score = -1
            #computer_score = -1

            for i in range(2):
                user_cards.append(deal_card())

            user_score = calculate_score(user_cards)
            print(f"\tYour cards: {user_cards}, current score = {user_score}")

            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            print(f"\tComputer\'s first card: {computer_cards[0]}")


            while not game_over:
                if sum(user_cards) > 21 or user_score == 0 or computer_score == 0:
                    game_over = True
                else:
                    play_again = input("Type \'y\' to get another card, type \'n\' to pass: ")

                    if play_again == 'y':
                        user_cards.append(deal_card())
                        user_score = calculate_score(user_cards)
                        print(f"\tYour cards: {user_cards}, current score = {user_score}")
                        print(f"\tComputer\'s first card: {computer_cards[0]}")

                    else:
                        game_over = True

            while computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)

            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"   Your final hand: {user_cards}, final score: {user_score}")
            print(f"   Computer\'s final hand: {computer_cards}, final score: {computer_score}")
            print(compare_score(user_score, computer_score))

        else:
            break

    #return


play_game()