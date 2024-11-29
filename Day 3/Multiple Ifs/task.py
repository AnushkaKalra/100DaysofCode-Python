print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")

    age = int(input("What is your age? "))
    if age <= 12:
        amount = 5
        print("Child tickets cost $5.")
    elif age <= 18:
        amount = 7
        print("Youth tickets cost $7.")
    else:
        amount = 12
        print("Adult tickets cost $12.")

    wantPhotos = input("Do you want photos? Please write \'Yes\' or \'No\': " )
    if wantPhotos == "Yes":
        amount += 3

    print(f"Your total bill is ${amount}.")

else:
    print("Sorry you have to grow taller before you can ride.")
