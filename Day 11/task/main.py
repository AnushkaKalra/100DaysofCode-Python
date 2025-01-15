import art
import random

while True:
    play = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")
    if play == 'y':
        should_continue = True
        while should_continue:
            print(art.logo)
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            #yes_count = 1

            user_cards = random.choices(cards, k=2)

            print(f"\tYour cards: {user_cards}, current score = {sum(user_cards)}")

            computer_cards = []
            computer_first_card = random.choice(cards)
            computer_cards.append(computer_first_card)
            print(f"\tComputer\'s first card: {computer_first_card}")

            if sum(user_cards) <= 21 or sum(computer_cards) <= 21:
                while sum(user_cards) <= 21:
                    play_again = input("Type \'y\' to get another card, type \'n\' to pass: ")
                    if play_again == 'y':
                        #yes_count += 1

                        user_cards.append(random.choice(cards))
                        print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")

                        computer_cards.append(random.choice(cards))
                        print(f"\tComputer\'s first card: {computer_first_card}")
                    else:
                        break

                print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"\tComputer\'s final hand: {computer_cards}, final score: {sum(computer_cards)}")


            if sum(user_cards) > 21:
                print(f"You went over. You lose!")
                break
                #should_continue = True

            elif sum(user_cards) > sum(computer_cards):
                print("You win 😃")
                break

            elif sum(user_cards) == sum(computer_cards):
                print("Draw 🙃")
                break
                #should_continue = True

            elif sum(user_cards) < sum(computer_cards):
                print("You lose 😤")
                break

            elif sum(user_cards) == 0:
                print("Win with a Blackjack 😎")
                break

            elif sum(computer_cards) == 0:
                print("Lose, opponent has Blackjack 😱")
                break

            else:
                print("Opponent went over. You win 😁")
                break
                #should_continue = True

    else:
        should_continue = False
        break