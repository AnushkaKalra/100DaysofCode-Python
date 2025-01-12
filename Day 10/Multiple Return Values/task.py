'''
Empty Returns
You can also write return without anything afterwards, and this just tells the function to exit.
'''


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return      # This will bypass the remaining code of the function and informs the function to exit.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"The name is: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
