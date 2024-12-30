def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
        
def go_back_build_wall():
    turn_around()
    move()
    turn_left()
    build_wall()
    turn_left()
    move()
    
# main

move()
move()
move()
turn_right()
move()
while not at_goal():
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
            continue
    if not wall_on_right():
        
        if at_goal():
            done()
        else:
            move()
            if wall_on_right():
                go_back_build_wall()
            elif wall_in_front():
                turn_left()
                continue
            else:
                turn_right()
                continue
            

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
