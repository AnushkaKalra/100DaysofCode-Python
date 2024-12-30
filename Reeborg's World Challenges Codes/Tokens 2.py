while not at_goal():
    move()
    if object_here():
        take()
        move()
        put()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
