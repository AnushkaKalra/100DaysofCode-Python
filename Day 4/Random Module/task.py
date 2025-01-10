import random

# Random Whole Numbers Within a Range
print("Random Integer:",random.randint(1,100)) # both 1 and 100 are inclusive

# Random Floats
rand_num_0_to_1 = random.random() # will generate a random float between 0.0 (inclusive) and 1.0 (not inclusive)
print("Random Float between 0 and 1:", rand_num_0_to_1)

rand_num_0_to_10 = random.random() * 10 # this will expand the range between 0.0 <= random_number < 10.0
print("Random Float between 0 and 10:", rand_num_0_to_10)

random_float = random.uniform(1, 100) # Another way to generate random floating point numbers. May or may not include upper bound limit
# In general, a <= random.uniform(a,b) <= b
print("Random Float between 0 and 100:", random_float)

print("HEADS OR TAILS")

choice = random.randint(0,1)
if choice == 0:
    print("Heads")
else:
    print("Tails")