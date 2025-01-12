def format_name(f_name, l_name):
    """ This function takes 2 inputs: f_name that signifies first name and
    l_name that signifies last name. Both the inputs are then converted to
    title case using title() function and returned as output."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
print(f"Name: {formatted_name}")

length = len(formatted_name)
print(f"Length of Name: {length}")

