from art import logo


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    n1 = float(input("What\'s the first number?: "))
    accumulate = True

    while accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        n2 = float(input("What\'s the next number?: "))

        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")

        should_continue = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ")
        if should_continue == 'y':
            accumulate = True
            n1 = result
        else:
            accumulate = False
            print('\n' * 5)
            calculator()

calculator()

