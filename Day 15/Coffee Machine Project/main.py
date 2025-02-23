MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#def print_report()

def calculate_amount(quarters, dimes, nickels, pennies):
    dollars = 0.00
    dollars += ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    cost_of_item = MENU[user_coffee_choice]["cost"]
    print(cost_of_item)

    remaining_amount = round(dollars - cost_of_item, 2)
    return remaining_amount
    # quarters = 0.25 * dollars
    # dimes = 0.10 * dollars
    # nickels = 0.05 * dollars
    # pennies = 0.01 * dollars

should_continue = True
while should_continue:
    user_coffee_choice = input("What would you like? (espresso, latte, cappuccino): ")
    if user_coffee_choice == "off":
        should_continue = False
        break
    #elif user_coffee_choice == "report":

    else:
        print("Please insert coins.")
        quar = int(input("how many quarters?: "))
        dim = int(input("how many dimes?: "))
        nic = int(input("how many nickels?: "))
        penn = int(input("how many pennies? "))
        cost = calculate_amount(quar, dim, nic, penn)
        print(f"Here is ${cost} in change.")
        print(f"Here is your {user_coffee_choice} ☕. Enjoy!")
        should_continue = True