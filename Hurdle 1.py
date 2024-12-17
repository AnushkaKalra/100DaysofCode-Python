def turn_right():
    for i in range(3):
        turn_left()

for j in range(6):
    move()    # straight (right) - start

    turn_left()    # up
    move()

    turn_right()    # straight (right)
    move()

    turn_right()    # down
    move()

    turn_left()    # straight (right)

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
