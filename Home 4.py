def forward():
    move()
    move()
    move()

def left():
    turn_left()

def right():
    turn_left()
    turn_left()
    turn_left()

# start      # (4,1)

forward()    # (4,4)
left()
forward()    # (1,4)
right()
move()       # (1,5)
right()
forward()    # (4,5)
left()
forward()    # (4,8)
right()
move()       # (5,8)
right()
forward()    # (5,5)
left()
forward()    # (8,5)
right()
move()       # (8,4)
right()
forward()    # (5,4)
left()
forward()    # (5,1)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
