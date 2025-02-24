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
    "money": 0
}


def print_report(resc):
    print("Water:", resc["water"], "ml")
    print("Milk:", resc["milk"], "ml")
    print("Coffee:", resc["coffee"], "g")
    print("Money: $", resc["money"])


def check_resources(resc, choice):
    resources_present = True

    for ingredient, amount_needed in MENU[choice]["ingredients"].items():
        if resc[ingredient] < amount_needed:
            print(f"Total {ingredient.capitalize()}: {resc[ingredient]}")
            print(f"{ingredient.capitalize()} needed: {amount_needed}")
            print(f"Sorry, there is not enough {ingredient}.")
            resources_present = False

    if resources_present:
        for ingredient, amount_needed in MENU[choice]["ingredients"].items():
            resc[ingredient] -= amount_needed
        resc["money"] += MENU[choice]["cost"]

    return resources_present, resc

    # print(resc["water"], resc["milk"], resc["coffee"])

    # if resc["water"] < MENU[choice]["ingredients"]["water"]:
    #     print("Total Water: ", resc["water"])
    #     print("Water needed: ", MENU[choice]["ingredients"]["water"])
    #     print("Sorry there is not enough water.")
    #     resources_present = False

    # elif resc["milk"] < MENU[choice]["ingredients"]["milk"]:
    #     print("Total Milk: ", resc["milk"])
    #     print("Milk needed: ", MENU[choice]["ingredients"]["milk"])
    #     print("Sorry there is not enough milk.")
    #     resources_present = False

    # elif resc["coffee"] < MENU[choice]["ingredients"]["coffee"]:
    #     print("Total Coffee: ", resc["coffee"])
    #     print("Coffee needed: ", MENU[choice]["ingredients"]["coffee"])
    #     print("Sorry there is not enough coffee.")
    #     resources_present = False

    # else:
    #     resc["water"] -= MENU[choice]["ingredients"]["water"]
    #     resc["milk"] -= MENU[choice]["ingredients"]["milk"]
    #     resc["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    #     resc["money"] += MENU[choice]["cost"]
    #     resources_present = True
    # return resources_present, resc


def calculate_amount(quarters, dimes, nickels, pennies):
    dollars = 0.00
    dollars += ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    cost_of_item = MENU[user_coffee_choice]["cost"]
    print(f"Amount deposited by the user: {dollars}")
    print(f"Cost of the item: {cost_of_item}")

    remaining_amount = round(dollars - cost_of_item, 2)
    is_amount_enough = True

    if remaining_amount > 0:
        return remaining_amount, is_amount_enough
    else:
        is_amount_enough = False
        print("Sorry that\'s not enough money. Money refunded.")
        # resc["money"] -= MENU[user_coffee_choice]["cost"]
        return cost_of_item, is_amount_enough


should_continue = True
while should_continue:
    user_coffee_choice = input("What would you like? (espresso, latte, cappuccino): ")
    if user_coffee_choice == "off":
        should_continue = False
        break

    elif user_coffee_choice == "report":
        print_report(resources)


    else:
        # print(check_resources(resources, user_coffee_choice))
        if not (check_resources(resources, user_coffee_choice)[0]):
            should_continue = True
            # break
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