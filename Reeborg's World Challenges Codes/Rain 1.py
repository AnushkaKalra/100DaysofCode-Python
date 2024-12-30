def turn_right():
    for i in range(3):
        turn_left()
    
def go_forward():
    while wall_on_right() and front_is_clear():
        move()
        if not wall_on_right():
            turn_right()
            build_wall()
        else:
            continue
    

# main        
move()
turn_right()
move()
while not at_goal():
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()
        go_forward()
if at_goal():
    done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
