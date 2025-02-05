'''
The concept of local and global scope doesn't just apply to variables. It also applies to functions, and basically anything that is defined/named by the user.
This concept is called NAMESPACE.
Namespace is valid in certain scopes.
'''

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) -> local variable

# Can't access this potion_strength outside its scope --> it will generate name error

# Global Scope

'''
Global variables and Local variables differ by where they are defined. Local variable is local to the function it is defined in,
while Global variable is defined outside a function.
Global variables are available within functions no matter how deep it gets nested, and its also available outside functions.
'''

player_health = 10  # global variable


def game():
    def drink_potion():  # local function
        potion_strength = 2  # local variable
        print(player_health)

    drink_potion()  # calling the local function


print(player_health)

'''
Note: 
Where you write the line of code that names the variable, defines the scope of that particular variable.
'''