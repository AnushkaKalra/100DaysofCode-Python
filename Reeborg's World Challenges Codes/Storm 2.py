def turn_right():
    for i in range(3):
        turn_left()
        
def turn_around():
    if wall_in_front() and wall_on_right():
        turn_left()
        move()
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
        if is_facing_north():
            move()
            turn_right()
        else:
            turn_left()
            turn_left()
            move()
            turn_left()
       
def around_garden():
    while front_is_clear():
        move()
        if object_here():
            while object_here():
                take()
                continue
    if wall_in_front() or wall_on_right():
        turn_around()
       
for i in range(5):
    around_garden()
while front_is_clear():
    move()
    if object_here():
        while object_here():
            take()
            continue
if wall_in_front():
    turn_left()
for step in range(3):
    move()
while object_here():
    take()
while carries_object():
    toss()
turn_left()
move()
turn_right()
move()
move()
turn_right()
move()

        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################


'''
Version 2
'''

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()
    

def move_around_garden():
    turn_left()
    if not is_facing_north():
        #move()
        #turn_left()
        #fix_one_row()
    #else:
        turn_around()
        move()
        turn_right()
        fix_one_row()
 
def fix_carrots():
    while object_here():
        take()
    if step<6:
        put()
    else:
        move_around_garden()
        
def fix_one_row():
    step = 0
    if object_here():
        step = 1
        fix_carrots()
    while step<6:
        move()
        step += 1
        fix_carrots()
        continue

    

    # step = 0
    # while step<6:
    #     #while front_is_clear():
    #     move()
    #     step += 1
    #     while object_here():
    #         take()
    #     put()
    #     #print(step)
    #     #continue
        
    # else:
    #     move_around_garden()
        
    
        
        
turn_left()
move()
move()
turn_right()
move()
#move()
for i in range(6):
    fix_one_row()
# if wall_in_front():
#     turn_around()
