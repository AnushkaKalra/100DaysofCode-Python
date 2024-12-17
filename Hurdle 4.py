def turn_right():
    for i in range(3):
        turn_left()

def jump():
    hurdle_height = 0
    turn_left()
    while wall_on_right():
        move()
        hurdle_height += 1
    turn_right()
    move()
    turn_right()
    for h in range(hurdle_height,0,-1):
        move()
    turn_left()
    
# main
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
