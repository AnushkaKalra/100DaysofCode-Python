def turn_right():
    for i in range(3):
        turn_left()

def fix_one_row():
    while front_is_clear():
        for step in range(6):
            
            while object_here():
                take()
            put()
            move()
        move()
        #move()
    if wall_in_front():
        if is_facing_north():
            turn_right()
            move()
            turn_right()
            move()
            move()
        else:
            turn_left()
            move()
            turn_left()
            move()
            move()

move()
move()
turn_left()
move()
move()
for i in range(6):
    fix_one_row()
done()

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
