object_count = 0

while not at_goal():
    if object_here():
        take()
        object_count += 1
        move()
    
    elif not object_here():
        for i in range(object_count):
            put()
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
