try:
    age = int(input("How old are you? "))
except ValueError:  # except Name_of_the_Error encountered while running the bug with faulty values
    print("You have encountered a Value Error as the input is not a valid number. Please try again with a numerical response like 18.")
    age = int(input("How old are you? "))

if age >= 18:
    print(f"You can drive at age {age}.")
