import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#First option
random_friend = random.choice(friends)
print(f"The friend is {random_friend}.")

#Second option
index = random.randint(0, len(friends)-1)  #len(friends)-1 to avoid Index Error because in randint, both a and b are inclusive.
print(index)
print(f"The friend is {friends[index]}.")

'''
Imp. functions for lists/sequences

1. random.choice(seq)
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

2. random.shuffle(x)
Shuffle the sequence x in place.
To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.
'''

'''
Imp. functions for integers

1. random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

2. random.randrange(stop)
random.randrange(start, stop[, step])
Return a randomly selected element from range(start, stop, step).
'''

'''
Imp. functions for floating point numbers i.e. real-valued distributions

1. random.random()
Return the next random floating-point number in the range 0.0 <= X < 1.0

2. random.uniform(a, b)
Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
The end-point value b may or may not be included in the range depending on floating-point rounding in the expression a + (b-a) * random().
'''

'''
Imp. function for bytes

1. random.randbytes(n)
Generate n random bytes.
'''