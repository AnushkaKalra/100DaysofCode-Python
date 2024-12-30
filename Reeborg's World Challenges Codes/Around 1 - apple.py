move()
while not object_here("apple"):
    while front_is_clear():
        move()
        if object_here("apple"):
            take()
        elif at_goal():
            done()
        else:
            continue
    if wall_in_front():
        turn_left()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
