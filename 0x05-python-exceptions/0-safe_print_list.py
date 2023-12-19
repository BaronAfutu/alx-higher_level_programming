#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): List to be printed from.
        x (int): Number of elements in my_list to print.

    Returns:
        Number of elements printed.
    """
    e_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            e_print += 1
        except IndexError:
            break
    print("")
    return (e_print)
