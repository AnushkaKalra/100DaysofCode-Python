think(50)
def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    repeat 3:
        turn_left()        
    
def toss_the_leaves():
    turn_around()
    while front_is_clear():
        move()
    if at_goal():
        turn_right()
        while carries_object():
            toss()
        else:
            done()

def go_around():                
    turn_right()
    move()
    move()
    turn_right()
    move()
    turn_left()

def go_to_yard():
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_right()
    while front_is_clear():
        if object_here():
            take()
        else:
            move()
    else:
        while object_here():
            take()
        else:
            turn_right()
            move()
            turn_right()

go_to_yard()

while True:
    if not front_is_clear():
        if is_facing_north():
            while object_here():
                take()
            else:
                turn_right()
                if wall_in_front():
                    turn_right()
                    while front_is_clear():
                        move()
                    else:
                        turn_left()
                        toss_the_leaves()
                move()
                turn_left()
                if front_is_clear():
                    move()
                    move()
                    turn_left()
                    move()
                    turn_right()
                else:
                    turn_around()
        else:
            while object_here():
                take()
            else:
                turn_left()
                if wall_in_front():
                    toss_the_leaves()
                else:
                    move()
                    if right_is_clear():
                        turn_right()
                        move()
                        move()
                        turn_right()
                        move()
                        turn_left()
                    else:
                        turn_left()
    elif object_here():
        take()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

# '''
# Version 2
# '''

# def turn_right():
#     for i in range(3):
#         turn_left()

# def turn_around():
#     turn_left()
#     turn_left()
    

# def move_around_garden():
#     turn_left()
#     if not is_facing_north():
#         #move()
#         #turn_left()
#         #fix_one_row()
#     #else:
#         turn_around()
#         move()
#         turn_right()
#         fix_one_row()
 
# def fix_carrots():
#     while object_here():
#         take()
#     if step<6:
#         put()
#     else:
#         move_around_garden()
        
# def fix_one_row():
#     step = 0
#     if object_here():
#         step = 1
#         fix_carrots()
#     while step<6:
#         move()
#         step += 1
#         fix_carrots()
#         continue

    

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
        
    
        
        
# turn_left()
# move()
# move()
# turn_right()
# move()
# #move()
# for i in range(6):
#     fix_one_row()
# # if wall_in_front():
# #     turn_around()