def find_maximum_bid(bid_dictionary):
    highest_bidder = None
    maximum_bid = float('-inf')

    #print(bid_dictionary)

    for key, value in bid_dictionary.items():
        if value > maximum_bid:
            highest_bidder = key
            maximum_bid = value

    print(f"The winner is {highest_bidder} with a bid of ${maximum_bid}.")


def bid_round(bid_dictionary):
    continue_bidding = True

    while continue_bidding:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: "))
        bid_dictionary[name] = bid
        others = input("Are there any other bidders? Type \'yes\' or \'no\': ")

        if others == 'yes':
            continue_bidding = True
            continue
        else:
            continue_bidding = False
            break

    find_maximum_bid(bid_dictionary)
    return bid_dictionary

# main
from art import logo
print(logo)
bid_dictionary = {}

bid_round(bid_dictionary)