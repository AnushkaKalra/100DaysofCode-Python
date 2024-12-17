def turn_right():
    for i in range(3):
        turn_left()

# main
if at_goal():
    done()
else:
    while not at_goal():
        while wall_on_right():
            if front_is_clear():
                move()
            elif wall_in_front():
                turn_left()
        if right_is_clear():
            turn_right()
            if at_goal():
                done()
            else:
                move()
        elif front_is_clear():
            move()

        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
