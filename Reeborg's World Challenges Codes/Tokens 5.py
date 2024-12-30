while not at_goal():
    move()
    if object_here():
        take()
    else:
        if carries_object():
            while carries_object():
                put()
                
if at_goal():
    done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
