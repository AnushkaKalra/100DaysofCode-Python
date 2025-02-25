print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_bill = 0

# Billing based on Pizza Size
if size.capitalize() == "S":
    total_bill += 15
elif size.capitalize() == "M":
    total_bill += 20
elif size.capitalize() == "L":
    total_bill += 25
else:
    print("Please choose a valid pizza size.")

# Billing based on Pepperoni
if size.upper() == "S":
    if pepperoni.upper() == "Y":
        total_bill += 2
    else:
        total_bill += 0

elif size.upper() == "M" or size.upper() == "L":
    if pepperoni.upper() == "Y":
        total_bill += 3
    else:
        total_bill += 0

# Billing based on Cheese
if extra_cheese.upper() == "Y":
    total_bill += 1
else:
    total_bill += 0

# Final Billing
print(f"Your final bill is: ${total_bill}. ")