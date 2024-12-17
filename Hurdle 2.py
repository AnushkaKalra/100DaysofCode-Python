def turn_right():
    for i in range(3):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    if at_goal():
        print(f"Number of hurdles crossed: {6 - number_of_hurdles}")
        done()
    else:
        jump()
    number_of_hurdles -= 1

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
