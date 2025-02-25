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


def check_resources(resc, choice):
    """Checks if enough resources (in terms of ingredients) are present in the coffee machine to make coffee."""

    resources_present = True

    for ingredient, amount_needed in MENU[choice]["ingredients"].items():
        if resc[ingredient] < amount_needed:
            print(f"Total {ingredient.capitalize()} available: {resc[ingredient]}")
            print(f"{ingredient.capitalize()} needed: {amount_needed}")
            print(f"Sorry, there is not enough {ingredient}.")
            resources_present = False

    return resources_present


def calculate_amount():
    """Calculates amount paid by the user to make coffee."""

    dollars = 0.00
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies? "))
    dollars += ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    return dollars


def is_transaction_valid(amount_deposited_by_user):
    """Checks if amount paid by the user is enough to make the coffee desired by the user. If yes, transaction is processed and change (if any) is given to the user.
    Else, the amount is refunded and given back to the user."""

    cost_of_drink = MENU[user_coffee_choice]["cost"]

    # print(f"Amount deposited by the user: {amount_deposited_by_user}")
    # print(f"Cost of the item: {cost_of_drink}")

    if amount_deposited_by_user >= cost_of_drink:
        is_amount_enough = True
        change_amount = round(amount_deposited_by_user - cost_of_drink, 2)
        print(f"Here is ${change_amount} in change.")

        global profit
        profit += cost_of_drink

    else:
        is_amount_enough = False
        print("Sorry that\'s not enough money. Money refunded.")

    return is_amount_enough


# main

profit = 0
should_continue = True

while should_continue:

    print()
    user_coffee_choice = input("What would you like? (espresso, latte, cappuccino): ")

    if user_coffee_choice == "off":
        should_continue = False
        break

    elif user_coffee_choice == "report":
        # print_report(resources)
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print("Money: $", profit)


    else:
        # print(check_resources(resources, user_coffee_choice))

        if not (check_resources(resources, user_coffee_choice)):
            should_continue = True


        else:
            drink = MENU[user_coffee_choice]
            if check_resources(resources, user_coffee_choice):
                payment_by_user = calculate_amount()
                if is_transaction_valid(payment_by_user):
                    # Deducts resources only AFTER payment is successful
                    for ingredient, amount_needed in MENU[user_coffee_choice]["ingredients"].items():
                        resources[ingredient] -= amount_needed

                    print(f"Here is your {user_coffee_choice} ☕. Enjoy!")
                    should_continue = True
