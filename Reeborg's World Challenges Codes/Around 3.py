def turn_right():
    for i in range(3):
        turn_left()

def jump():
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    
    
# main

put()
turn_left()
jump()
turn_left()
while not object_here():
    while front_is_clear():
        move()
        if object_here():
            done()
        elif right_is_clear():
            turn_right()
        continue
    if wall_in_front():
        turn_left()
        continue


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
