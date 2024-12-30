def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
        
def collect_leaves():
    while wall_on_right():
        if object_here():
            take()
            continue
        elif wall_in_front():
            turn_around()
            continue 
        else:
            move()   

while front_is_clear():
    if object_here():
        collect_leaves()
    move()

if wall_in_front() and carries_object():
    turn_right()
    while carries_object():
        toss()
    done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
