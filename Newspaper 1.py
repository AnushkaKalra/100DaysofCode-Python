def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
        
def up_three_steps():
    for step in range(3):
        turn_left()
        move()
        turn_right()
        for j in range(2):
            move()
            
def down_three_steps():
    for step in range(3):
        for j in range(2):
            move()
        turn_left()
        move()
        turn_right()
# main
take()
up_three_steps()
put()
while object_here("token"):
    take("token")
turn_around()
down_three_steps()     
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
