put()
move()
while not object_here():
    while front_is_clear():
        move()
        if object_here():
            done()
        continue
    if wall_in_front():
        turn_left()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
