# Accessible anywhere
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    print(f"Local Variable: {my_local_var}")

my_function()

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3
print(f"Global Variable: {my_block_var}")


