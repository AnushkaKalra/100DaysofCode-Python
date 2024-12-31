def turn_around():
    for i in range(2):
        turn_left()


step_count = 0
while front_is_clear():
    move()
    step_count += 1
if not (front_is_clear() and right_is_clear()):
    turn_around()

for step in range(step_count,0,-2):
    move()
put()
done()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
