def go_forward():
    for i in range(6):
        move()
    
def turn_around():
    turn_left()
    turn_left()

def return_back():
    for i in range(5):
        move()

# main        
go_forward()
build_wall()
turn_around()
return_back()
turn_around()    # optional
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
