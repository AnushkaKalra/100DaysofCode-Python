programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Retrieving a value from the dictionary
print(programming_dictionary["Bug"])

# Adding a value to the dictionary
programming_dictionary["Variable"] = "A container for storing data values."
print(f"Dictionary after adding a value: {programming_dictionary}")

# Modifying a value in the dictionary
programming_dictionary["Variable"] = "A container for storing data values. It is the basic building block of programming."
print(f"Dictionary after modifying a value: {programming_dictionary}")

# Looping through the dictionary for keys
print("Keys:")
for key in programming_dictionary:
    print(key)

# Looping through the dictionary for values
print("Values:")
for key in programming_dictionary:
    print(programming_dictionary[key])