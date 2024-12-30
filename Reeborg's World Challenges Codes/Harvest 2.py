def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    if is_facing_north() and wall_on_right():
        turn_left()
    else:
        turn_right()
        
def harvest_one_row():
    while front_is_clear():
        move()
        while object_here():
            take()
        continue
    if wall_in_front():
        turn_left()
        if is_facing_north():
            move()
            turn_around()
        else:
            turn_left()
            turn_left()
            move()
            turn_around()
        
        
turn_left()
move()
move()
turn_right()
for i in range(6):
    harvest_one_row()
if wall_in_front():
    turn_around()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
