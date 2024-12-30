def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()
    
step = 1
while front_is_clear():
    move()
    step += 1
mid = (step+1)//2
#print(mid)
    
turn_around()
for i in range(mid,1,-1):    # not for i in range(mid,0,-1) because initial value of step = 1
    move()
turn_right()

if front_is_clear():    
    for j in range(mid,0,-1):
        move()
    
put()    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
