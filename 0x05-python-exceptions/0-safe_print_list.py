#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = x
    try:
        for i in range(x):
            print("{}".format(my_list[i], end=""))
        print()
        return count
    except IndexError:
        print()
        return count
