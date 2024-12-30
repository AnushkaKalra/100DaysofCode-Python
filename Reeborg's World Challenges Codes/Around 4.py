def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
        
def jump():
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_right()
    move()
    move()
    
# main

put()
turn_around()
move()
turn_right()
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
