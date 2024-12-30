def turn_right():
    for i in range(3):
        turn_left()

# main

put()
move()
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


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
