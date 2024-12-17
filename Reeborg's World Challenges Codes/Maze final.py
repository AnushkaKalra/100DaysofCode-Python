def turn_right():
    for i in range(3):
        turn_left()

# main
while not at_goal():
    while wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    if right_is_clear():
        if at_goal():
            done()
        else:
            turn_right()
            move()
    elif front_is_clear():
        move()

        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
